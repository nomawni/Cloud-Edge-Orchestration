import paho.mqtt.client as mqtt
import time
import ssl
import os
from pathlib import Path


def on_connect(client, userdata, flag, rc):

    if rc == 0:
        client.connected_flag = True
        print("Connected to broker")
    else:
        print("Connection failed")


def mqtt_connection_handler():
    mqtt.Client.connected_flag = False
    client = mqtt.Client(
        "271c1595-8c09-4277-acc0-4b244e62f8b4", clean_session=False)
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

    client.loop_start()
    print("Connecting to broker")

    client.connect("a2znsji32awrj2-ats.iot.us-west-2.amazonaws.com", 8883)
    #client.connect("141.13.5.136", 1883)

    while not client.connected_flag:
        print("Waiting for connection")
        time.sleep(1)

    print("Main Loop")
    client.publish("services/cpuLoadSvc/<MQTT_CLIENT_ID>/jobs/read/req")
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    mqtt_connection_handler()
