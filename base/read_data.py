import os

import yaml

class ReadData(object):
    """读取数据"""

    def read_yaml_data(self, name):
        # with open(os.getcwd() + os.sep + 'data' + os.sep + name, encoding='utf-8') as f:
        # with open('E:\\3_app_code\\day07\\set\\data\\test_data.yml',encoding='utf-8') as f:
        with open('.' + os.sep + 'data' + os.sep + name, encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data
