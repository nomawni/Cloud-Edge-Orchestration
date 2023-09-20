import os

class AWSThing:
    def __init__(self, thing_name:str, thing_type:str, thing_arn:str, thing_attributes):
        self.thing_name = thing_name
        self.thing_type = thing_type
        self.thing_arn = thing_arn
        self.thing_attributes = thing_attributes
    
    def create_thing(self) -> None:
        print("Creating thing")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot create-thing --thing-name {} --thing-type {}".format(self.thing_name, 
        self.thing_type))

    def create_certificate(self):
        print("Creating certificate")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile {}".format(self.thing_name))

    def update_certificate(self):
        print("Updating certificate")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot update-certificate --certificate-id {}".format(self.thing_name))
    
    def delete_certificate(self):
        print("Deleting certificate")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot delete-certificate --certificate-id {}".format(self.thing_name))
    
    def attach_policy(self):
        print("Attaching policy")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot attach-policy --policy-name {} --target {}".format(self.thing_name, 
        self.thing_arn))

    def detach_policy(self):
        print("Detaching policy")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot detach-policy --policy-name {} --target {}".format(self.thing_name, 
        self.thing_arn))
    
    def describe_thing(self):
        print("Describing thing")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot describe-thing --thing-name {}".format(self.thing_name))
    
    def describe_thing_type(self):
        print("Describing thing type")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot describe-thing-type --thing-type-name {}".format(self.thing_type))
    

    def update_thing(self):
        print("Updating thing")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot update-thing --thing-name {} --thing-type {}".format(self.thing_name, 
        self.thing_type))
    
    def delete_thing(self):
        print("Deleting thing")
        print("Thing name: {}".format(self.thing_name))
        print("Thing type: {}".format(self.thing_type))
        print("Thing arn: {}".format(self.thing_arn))
        print("Thing attributes: {}".format(self.thing_attributes))
        print("")
        os.system("aws iot delete-thing --thing-name {}".format(self.thing_name))