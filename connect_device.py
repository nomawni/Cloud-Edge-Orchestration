import os

class ConnectDevice:

    # authenticate device with ssh
    def authenticate_device(self, device_name, device_ip, device_username, device_password):
        print("Authenticating device")
        print("Device name: {}".format(device_name))
        print("Device ip: {}".format(device_ip))
        print("Device username: {}".format(device_username))
        print("Device password: {}".format(device_password))
        print("")
        os.system("sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{}".format(device_password, 
        device_username, device_ip))

    # connect to device
    def connect_device(self, device_name, device_ip, device_username, device_password):
        print("Connecting to device")
        print("Device name: {}".format(device_name))
        print("Device ip: {}".format(device_ip))
        print("Device username: {}".format(device_username))
        print("Device password: {}".format(device_password))
        print("")
        os.system("sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{}".format(device_password, 
        device_username, device_ip))

    # disconnect from device
    def disconnect_device(self, device_name, device_ip, device_username, device_password):
        print("Disconnecting from device")
        print("Device name: {}".format(device_name))
        print("Device ip: {}".format(device_ip))
        print("Device username: {}".format(device_username))
        print("Device password: {}".format(device_password))
        print("")
        os.system("sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{}".format(device_password, 
        device_username, device_ip))
    



    
