import os


def current_dir():
    env_dir_path = os.path.dirname(os.path.realpath(__file__))
    env_path = os.path.join(env_dir_path, '.env')
    env_dir_file_path = os.path.join(env_dir_path, 'env_path_exporter.py')
    #os.system("export ENV_FILE_PATH={}".format(env_path))
    #os.system("export ENV_FILE_EXPORTER_PATH={}".format(env_dir_file_path))


if __name__ == "__main__":

    current_dir()
    print("--------------------")
    print(os.path.join(os.getcwd(), 'edge_iot_simulator/env_path_exporter.py'))
