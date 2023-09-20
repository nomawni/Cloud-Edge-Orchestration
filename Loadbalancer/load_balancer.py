from haproxy_handler import delete_backend_server, get_existing_backend_servers, get_backends, create_server
import os
import sys
import json
import yaml
from docker_run_edge_containers import EdgeContainers
from update_env_file import EnvFileHandler
# index of which container to run next
index = 0


class LoadBalancer:
    def __init__(self, mqtt_client):
        self.sleep_time = 5
        self.r = None
        self.mqtt_client = mqtt_client

    def load_balancer(self, message):

        try:
            # s = requests.Session()
            res = json.loads(str(message.payload.decode("utf-8")))
            data = res['sucess']
            if data:
                sum_cpu_loads = 0
                for k, v in res.items():
                    sum_cpu_loads += int(v["target_load"])
                # check if the sum is greater than 65
                if sum_cpu_loads > 65:
                    # increment the index by 1 to get the next container
                    index += 1
                    # get the server info
                    container_name, dockerfile_directory, container_network = self.get_server_info(
                        index)
                    # create the container
                    edge_containers = EdgeContainers()
                    edge_containers.scale_on_new_container(
                        container_name, dockerfile_directory, container_network)
                    create_server(container_name)
                    mqtt_client_id = EnvFileHandler().get_device_client_id()
                    self.mqtt_client.subscribe(
                        "services/cpuLoadSvc/{}/jobs/read/req".format(mqtt_client_id), qos=1)
                    # print("create server")
                # check if the sum is less than 15
                elif sum_cpu_loads < 15:
                    delete_backend_server()
                    # print("delete server")
                print("sum_cpu_loads: {}".format(sum_cpu_loads))

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()

    def get_server_info(self, server_index):

        with open("docker_config_edge.yml", "r") as f:
            try:
                config = yaml.safe_load(f)
                list_containers = config["containers"]["list"]
                list_keys = list(config["containers"]["list"])
                container_name = list_keys[server_index]
                dockerfile_directory = list_containers[container_name]["directory"]
                container_network = list_containers[container_name]["network"]
                # return the server info
                return (container_name, dockerfile_directory, container_network)
            except yaml.YAMLError as exc:
                print(exc)
