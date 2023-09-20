import paho.mqtt.client as mqtt
import time
import ssl
import os
from pathlib import Path
import logging
import json
from load_balancer import load_balancer


def on_connect(client, userdata, flag, rc):

    if rc == 0:
        #client.connected_flag = True
        print("Connected to broker")
        #res = client.subscribe("services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/req",1)
        client.subscribe(
            "services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/res", qos=1)
        # print(res)
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print("received message =", str(message.payload.decode("utf-8")))
    load_balancer(message)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe on the topic")
    pass


def on_publish(client, userdata, result):
    print("data published \n")
    pass


def on_disconnect(client, userdata, rc):
    logging.info("disconnecting reason " + str(rc))


def mqtt_connection_handler():
    mqtt.Client.connected_flag = False
    client = mqtt.Client(
        "d8bc00a7-2bd1-48bf-a0cd-653d0626937b", clean_session=False)
    #client = mqtt.Client("1b93c60e-aa89-43f6-8706-89a6a7e7df0b", clean_session=False)
    # os.path.join("/certs","AmazonRootCA1.pem")
    ca_cert = Path("./../certs/AmazonRootCA1.pem")
    print('ca_cert: {}'.format(ca_cert))
    # os.path.join("/certs", "device.pem.crt")
    certfile = Path("./../certs/device.pem.crt")
    print('certfile: {}'.format(certfile))
    # os.path.join("/certs", "private.pem.key")
    keyfile = Path("./../certs/private.pem.key")
    client.tls_set(ca_certs=ca_cert,
                   certfile=certfile, keyfile=keyfile,
                   tls_version=ssl.PROTOCOL_TLSv1_2, cert_reqs=ssl.CERT_OPTIONAL)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    # client.loop_start()
    print("Connecting to broker")

    client.connect("a2znsji32awrj2-ats.iot.us-west-2.amazonaws.com", 8883)
    #client.connect("141.13.5.136", 1883)

    # while not client.connected_flag:
    #    print("Waiting for connection")
    #    time.sleep(1)

    print("Main Loop")
    #res = client.publish("services/cpuLoadSvc/*/jobs/read/req","Hello, how are you",1)
    #res = client.subscribe("sensors/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/data",qos=1)
    # while(True):
    client.publish(
        "services/cpuLoadSvc/1b93c60e-aa89-43f6-8706-89a6a7e7df0b/jobs/read/req", qos=1)
    #    time.sleep(5)
    # print(res)
    # print(res[0])
    # print(res[1])
    # logging.info(res)
    client.loop_forever()
    # client.loop_stop()
    # client.disconnect()


if __name__ == "__main__":
    mqtt_connection_handler()
