from haproxy_handler import delete_backend_server, get_existing_backend_servers, get_backends, create_server
import os
import sys
import time
import requests
import logging
import warnings
import json


def load_balancer(message):

    # sleep_time = 5
    # url = "https://localhost:5000/"
    try:
        # s = requests.Session()
        res = json.loads(str(message.payload.decode("utf-8")))
        data = res['sucess']
        if data == True:
            sum_cpu_loads = 0
            for k, v in res.items():
                sum_cpu_loads += int(v["target_load"])

            # check if the sum is greater than 65
            if sum_cpu_loads > 65:
                create_server()
                # print("create server")
            # check if the sum is less than 15
            elif sum_cpu_loads < 15:
                delete_backend_server()
                # print("delete server")
            print("sum_cpu_loads: {}".format(sum_cpu_loads))

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

    """   while(True):
            # data = open(
             #   '/home/ibrahima-sory.sow/edge-iot-simulator/loadbalancer/list_servers.json', 'r')
            res = json.loads(str(message.payload.decode("utf-8")))
            # data = json.load(data)
            print('Getting all backends !!\n')
            get_backends()
            print('Getting existing backends !!\n')
            get_existing_backend_servers()
            print('Creating a server !!\n')
            create_server()
            for i in data['servers']:
                try:
                    r = s.get(i['server_url'], verify=False, timeout=30)
                    if r.status_code == 200:
                        print(r.text)
                        print(r.status_code)
                        break
                    else:
                        print(r.status_code)
                except requests.exceptions.ConnectionError as e:
                    logging.error(e)
                finally:
                    time.sleep(sleep_time)
            # get the measured temperature
            # response = s.get()
            """
