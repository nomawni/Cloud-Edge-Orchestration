import os
from docker_handler import DockerHandler
import yaml


class EdgeContainers:

    # when the cpu is over 65%, a new container will be run
    def scale_on_new_container(container_name, dockerfile_directory, container_network):
        # index of the container in the container list
        try:
            # change to directory edge_
            #os.system("cd {}".format(dockerfile_directory))
            os.chdir("./{}".format(dockerfile_directory))
            env_directory = os.path.join(
                os.getcwd(), "edge_iot_simulator/.env")
            os.system("export ENV_FILE_PATH={}".format(env_directory))
            dockerHandler = DockerHandler(container_name)
            #os.system("docker build -t {} {}".format(container_name, "."))
            dockerHandler.build_container(".")
            dockerHandler.run_container(
                "--network {}".format(container_network))
            os.chdir("../")
            # rn docker with network backend
            #os.system("docker run -d --name {} --newtwork={}".format(container_name, container_network))
        except yaml.YAMLError as exc:
            print(exc)
        except FileNotFoundError:
            print("Directory {} not found".format(dockerfile_directory))
        except NotADirectoryError:
            print("{} is not a directory".format(dockerfile_directory))
        except PermissionError:
            print("Permission denied")

    def download_and_configure_edge():
        # install necessary packages
        os.system("sudo apt-get install python3-flask python3-venv python3-wheel")
        # download the edge-iot-simulator
        os.system(
            "git clone https://gitlab.rz.uni-bamberg.de/sebastian.boehm/edge-iot-simulator")
        os.system("cd edge-iot-simulator")
        # copy .env-example to .env
        os.system("cp .env-example .env")
        os.system("cd ..")
        # create a virtual environment
        os.system("python3 -m venv venv")
        # activate the virtual environment
        os.system("source venv/bin/activate")
        # update pip
        os.system("pip install --upgrade pip")
        # install the necessary packages
        os.system("pip install -r requirements.txt")
        # change to dircetory edge-iot-simulator
        os.system("cd edge-iot-simulator")
        # run main.py
        os.system("python3 main.py")


if __name__ == "__main__":
    EdgeContainers.scale_on_new_container()
    """with open('list_pub_sub_topics.yml', 'r') as f:
        try:
            config = yaml.safe_load(f)

            list_topics = config["topics"]["ids"]
            list_keys = list(config["topics"]["ids"])
            for topic_id in list_topics:
                print(topic_id)

        except yaml.YAMLError as exc:
            print(exc) """
