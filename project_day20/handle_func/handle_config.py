from configparser import ConfigParser
import os
from handle_func.handle_path import CONF_DIR
class config(ConfigParser):
    def __init__(self,filename,encoding='utf-8'):
        super().__init__()
        self.read(filename,encoding=encoding)

# 创建一个配置文件解析器
config_path=os.path.join(CONF_DIR,'conf.ini')
conf=config(config_path)