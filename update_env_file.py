import uuid
import os
import argparse
import yaml


class EnvFileHandler:

    # Nee this client id to check the current cpu of the container
    def get_device_client_id(self):

        # return the client id
        env_file_path = os.environ['ENV_FILE_PATH']
        with open(env_file_path, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].startswith('MQTT_CLIENT_ID'):
                    client_id = lines[i].split('=')[1].strip()
                    self.add_client_id_to_pub_sub(client_id)
                    # return lines[i].split('=')[1].strip()
                    return client_id

    def add_client_id_to_pub_sub(self, client_id):
        with open('list_pub_sub_topics.yml', 'r') as f:
            data = yaml.safe_load(f)
            # add new value into yaml file
            data['topics']['ids'].append(client_id)
            yaml.dump(data, open('list_pub_sub_topics.yml', 'w'))

    def update_environment_file():

        clientId = uuid.uuid4()
        print(clientId)
        parser = argparse.ArgumentParser()
        parser.add_argument("EDGE", help="Edge name")
        edge_name = parser.parse_args().EDGE
        print("Edge name: {}".format(parser.parse_args().EDGE))
        # generate env file path
        os.system("python3 edge_iot_simulator/env_path_exporter.py")
        env_dir_path = os.environ['ENV_FILE_EXPORTER_PATH']
        print("env_dir_path: {}".format(env_dir_path))
        # os.system("python {}".format(env_dir_path))
        # generate MQTT client id
        # Read the .env file in the edge-iot-simulator directory
        # /home/ibrahima-sory.sow/edge-iot-simulator/loadbalancer/.env
        # env_file = os.environ["ENV_FILE_PATH"]
        env_path = os.environ["ENV_FILE_PATH"]
        print(env_path)
        with open('.env', 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].startswith('MQTT_CLIENT_ID'):
                    lines[i] = 'MQTT_CLIENT_ID={}\n'.format(clientId)

                elif lines[i].startswith('MQTT_CA_CERTS'):
                    lines[i] = 'MQTT_CA_CERTS={}\n'.format(
                        './' + edge_name + '/AmazonRootCA1.pem')
                elif lines[i].startswith('MQTT_CERTFILE'):
                    lines[i] = 'MQTT_CERTFILE={}\n'.format(
                        './' + edge_name + '/device.pem.crt')
                elif lines[i].startswith('MQTT_KEYFILE'):
                    lines[i] = 'MQTT_KEYFILE={}\n'.format(
                        './' + edge_name + '/private.pem.key')

        # Replace the clientId in the .env file
            # lines[0] = 'CLIENT_ID={}\n'.format(clientId)
           # Write the new .env file
            with open('.env', 'w') as f:
                f.writelines(lines)
            f.close()
        # rename Edge0 to certs
        # if os.path.isdir("certs"):
        #    os.rename("certs", edge_name)

        # last_char = edge_name[-1]
        # os.rename(edge_name, 'certs')
        # get the env file path


if __name__ == "__main__":
    EnvFileHandler.update_environment_file()
    # update_environment_file()
