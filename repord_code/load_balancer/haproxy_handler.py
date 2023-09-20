import imp
from unicodedata import name
import requests
import os
import logging
import time
import json

sleep_time = 5

#os.environ["PYTHONWARNINGS"] = "ignore"
s = requests.Session()

# function to get all the backends


def get_backends():
    try:
        r = s.get('https://141.13.5.136:5555/v2/services/haproxy/configuration/backends',
                  verify=False, timeout=30,
                  auth=('admin', 'password'))
        if r.status_code == 200:
            print(r.text)
            print(r.status_code)
        else:
            print(r.status_code)
    except requests.exceptions.ConnectionError as e:
        logging.error(e)
    finally:
        time.sleep(sleep_time)

# function to get all the existing backend servers


def get_existing_backend_servers():
    try:
        r = s.get('http://141.13.5.136:5555/v2/services/haproxy/configuration/servers?backend=iot-backend',
                  verify=False, timeout=30,
                  auth=('admin', 'password'))
        if r.status_code == 200:
            print(r.text)
            print(r.status_code)
        else:
            print(r.status_code)
    except requests.exceptions.ConnectionError as e:
        logging.error(e)
    finally:
        time.sleep(sleep_time)


def get_name_and_version():
    try:
        r = s.get('http://141.13.5.136:5555/v2/services/haproxy/configuration/servers?backend=iot-backend',
                  verify=False, timeout=30,
                  auth=('admin', 'password'))
        if r.status_code == 200:
            data = json.loads(r.text)
            return data["data"][-1]['name'], data['_version']
        else:
            print(r.status_code)
            return None, None
    except requests.exceptions.ConnectionError as e:
        logging.error(e)
    finally:
        time.sleep(sleep_time)


def delete_backend_server():
    try:
        (name, version) = get_name_and_version()
        if name is not None and version is not None:
            r = s.delete('http://141.13.5.136:5555/v2/services/haproxy/configuration/servers/{}?backend=iot-backend&version={}'.format(name, version),
                         verify=False, timeout=30,
                         auth=('admin', 'password'))
            if r.status_code == 200:
                print(r.text)
                print(r.status_code)
            else:
                print(r.status_code)
    except requests.exceptions.ConnectionError as e:
        logging.error(e)
    finally:
        time.sleep(sleep_time)


def create_server():
    try:
        (name, version) = get_name_and_version()
        if name is not None and version is not None:
            server_number = name[-1]
            server_name = 's{}'.format(int(server_number) + 1)
            # You should the path of the file absolute like the following:
            # /home/ibrahima-sory.sow/edge-iot-simulator/loadbalancer/list_servers.json
            list_servers_file = open('list_servers.json', 'r')
            list_servers = json.load(list_servers_file)
            server_pos = 0
            for server in list_servers['servers']:
                if server['selected'] == False:
                    server_url = server['server_url']
                    r = s.post('https://localhost:5555/v2/services/haproxy/configuration/servers?backend=iot-backend&version={}'.format(version),
                               verify=False, timeout=30,
                               auth=('admin', 'password'),
                               data=json.dumps(
                                   {"name": server_name, "address": "edge02", "port": "5000"}),
                               headers={'Content-Type': 'application/json'}
                               )
                    if r.status_code == 200:
                        print(r.text)
                        print(r.status_code)
                        list_servers_file.close()
                        with open('list_servers.json', 'w') as f:
                            # if the server is created, set the selected flag to True
                            list_servers.get('servers')[
                                server_pos]['selected'] = True
                            json.dump(list_servers, f)

                    else:
                        print(r.status_code)
                server_pos += 1

    except requests.exceptions.ConnectionError as e:
        logging.error(e)
    finally:
        time.sleep(sleep_time)
