import os

class HaproxyDocker:

    def __init__(self) -> None:
        
        self.image = "haproxy:1.7.5-alpine"
        self.container_name = "haproxy"
        self.command = "haproxy -f /etc/haproxy/haproxy.cfg"
        self.port = "80"
        self.sleep_time = 5
        self.verify = False
        self.timeout = 30
        self.auth = ('admin', 'password')
        self.r = None
        self.data = None
        self.name = None
        self.version = None
        self.url = None
        self.headers = {'Content-type': 'application/json'}
        self.payload = None
        self.r = None
        self.data = None
    
    def create_network(self):
        
        os.system("sudo docker network create --driver=bridge iot-network")
    
    def create_app(self):

        os.system("sudo docker run -d --name {} -p {}:80 --network iot-network {} {}"
        .format(self.container_name, self.port, self.image, self.command))
    
    def create_haproxy_container(self):

        os.system("sudo docker run -d --name haproxy -v $(pwd):/usr/local/etc/haproxy:ro -p 80:80 --network iot-network haproxytech/haproxy-alpine:2.4")

    def create_haproxy_config(self):

        os.system("sudo docker cp haproxy_config.cfg haproxy:/etc/haproxy/haproxy.cfg")
    
    def kill_haproxy(self):

        os.system("sudo docker kill -s HUP haproxy")