import os
import sys
import time
from venv import create
import requests
import logging
import warnings
import json
from haproxy_handler import delete_backend_server, get_existing_backend_servers, get_backends, create_server
sleep_time = 5
url = "https://localhost:5000/"
try:
    s = requests.Session()
    while(True):
        # TODO Please implement the following functions
        # 1- Check if the CPU of VM has exceeded the threshold 65% and if so, create new Server with the following function
        create_server()
        # 2- Check if the CPU of VM has exceeded the threshold 15% and if so, delete the Server with the following function
        delete_backend_server()
        # get_backends()
        # get_existing_backend_servers()
        # get the measured temperature
        #response = s.get()
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
