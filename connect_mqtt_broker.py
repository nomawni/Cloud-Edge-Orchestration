import paho.mqtt.client as mqtt
import time
import ssl
import os
from pathlib import Path
import logging
import json
from load_balancer import LoadBalancer
import yaml


class ConnectMQTTBroker:
    def __init__(self):
        self.client = None

    def subscribe_to_topic(self, topic):
        self.client.subscribe(topic, qos=1)

    def publish_to_topic(self, topic, payload=None):
        self.client.publish(topic, qos=1)

    def on_connect(self, client, userdata, flag, rc):
        if rc == 0:
            #client.connected_flag = True
            print("Connected to broker")
            #res = client.subscribe("services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/req",1)
            self.subscribe_to_topic(
                "services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/req")
            # client.subscribe(
            #    "services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/res", qos=1)
            # print(res)
        else:
            print("Connection failed")

    def on_message(self, client, userdata, message):
        print("received message =", str(message.payload.decode("utf-8")))
        LoadBalancer(self.client).load_balancer(message)
        # load_balancer(message)

    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribe on the topic")
        pass

    def on_publish(client, userdata, result):
        print("data published \n")
        pass

    def on_disconnect(client, userdata, rc):
        logging.info("disconnecting reason " + str(rc))

        with open('list_pub_sub_topics.yml', 'r') as f:
            try:
                config = yaml.safe_load(f)
                list_topics = config["topics"]["ids"]
                list_topics_size = len(list_topics)
                if list_topics_size > 1:
                    while(list_topics_size > 1):
                        config['topics']['ids'].pop()
                        list_topics_size = list_topics_size - 1
                    yaml.dump(config, open(
                        'list_pub_sub_topics.yml', 'w'))

            except yaml.YAMLError as exc:
                print(exc)

    def mqtt_connection_handler(self):
        mqtt.Client.connected_flag = False
        self.client = mqtt.Client(
            "d8bc00a7-2bd1-48bf-a0cd-653d0626937b", clean_session=False)
        # Please dynamically change the path of the certificate file and key file
        # the certificate file and key file are for the first edge, meaning the edge
        # that is running with haproxy
        ca_cert = Path("./../certs/AmazonRootCA1.pem")
        print('ca_cert: {}'.format(ca_cert))
        # os.path.join("/certs", "device.pem.crt")
        certfile = Path("./../certs/device.pem.crt")
        print('certfile: {}'.format(certfile))
        # os.path.join("/certs", "private.pem.key")
        keyfile = Path("./../certs/private.pem.key")
        self.client.tls_set(ca_certs=ca_cert,
                            certfile=certfile, keyfile=keyfile,
                            tls_version=ssl.PROTOCOL_TLSv1_2, cert_reqs=ssl.CERT_OPTIONAL)
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        # client.loop_start()
        print("Connecting to broker")

        self.client.connect(
            "a2znsji32awrj2-ats.iot.us-west-2.amazonaws.com", 8883)
        #client.connect("141.13.5.136", 1883)

        # while not client.connected_flag:
        #    print("Waiting for connection")
        #    time.sleep(1)

        print("Main Loop")
        #res = client.publish("services/cpuLoadSvc/*/jobs/read/req","Hello, how are you",1)
        #res = client.subscribe("sensors/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/data",qos=1)
        # while(True):
        #self.client.publish("services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/req", qos=1)
        while(True):
            # subscribe to list_pub_sub_topic
            # this is just a hack, not too efficent but it works
            with open('list_pub_sub_topics.yml', 'r') as f:
                try:
                    config = yaml.safe_load(f)

                    list_topics = config["topics"]["ids"]
                    for topic_id in list_topics:
                        self.publish_to_topic(
                            "services/cpuLoadSvc/{}/jobs/read/req".format(topic_id))
                        time.sleep(1)
                        print(topic_id)

                except yaml.YAMLError as exc:
                    print(exc)
            # self.publish_to_topic()
            time.sleep(10)
        self.publish_to_topic(
            "services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/req")
        self.client.loop_forever()


if __name__ == "__main__":
    mqtt_broker = ConnectMQTTBroker()
    mqtt_broker.mqtt_connection_handler()
