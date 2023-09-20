import os


class DockerHandler:

    def __init__(self, container_name, network="backend", image=None, port=5000):
        self.image = image
        self.container_name = container_name
        #self.command = command
        self.port = port

    def create_container(self):
        print("Creating container")
        print("Image: {}".format(self.image))
        print("Container name: {}".format(self.container_name))
        print("Command: {}".format(self.command))
        print("Port: {}".format(self.port))
        print("")
        os.system("docker run -d -p {}:80 --name {} {} {}".format(self.port,
                                                                  self.container_name, self.image))
    # build container from image

    def build_container(self, command=None):
        print("Building container")
        print("Container name: {}".format(self.container_name))
        print("Command: {}".format(command))
        print("")
        os.system("docker build -t {} {}".format(self.container_name, command))

    def run_container(self, command=None):
        print("Running container")
        print("Container name: {}".format(self.container_name))
        print("Command: {}".format(self.command))
        print("")
        os.system()
        os.system("docker run -d --name {} {}".format(
            self.container_name, command))

    def stop_container(self):
        print("Stopping container")
        print("Container name: {}".format(self.container_name))
        print("Command: {}".format(self.command))
        print("")
        os.system("docker stop {}".format(self.container_name))

    def remove_container(self):
        print("Removing container")
        print("Container name: {}".format(self.container_name))
        print("Command: {}".format(self.command))
        print("Port: {}".format(self.port))
        print("")
        os.system("docker rm {}".format(self.container_name))

    # run docker-compose
    def run_docker_compose(self):
        print("Running docker-compose")
        print("Container name: {}".format(self.container_name))
        print("Command: {}".format(self.command))
        print("Port: {}".format(self.port))
        print("")
        os.system("docker-compose up -d")
