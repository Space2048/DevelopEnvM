
#-*-coding:utf-8-*
from typing import Any
import yaml
import psutil
import os

def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


class SingletonMeta(type):
    _instances = {}
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            instance = super().__call__(*args, **kwds)
            self._instances[self] = instance
        return self._instances[self]


#配置类
class Config(metaclass=SingletonMeta):
    configLib = {}
    yamlFile = "./test/simple.yaml"
    def __init__(self):
        Config.injectDefaultConfig()
    
    def get(self, name):
        if name not in Config.configLib.keys():
            return None
        return Config.configLib[name]

    def set(self, name, value):
        if not name or not value:
            return None
        if name in Config.configLib.keys():
            return None
        Config.configLib[name] = value
    
    @staticmethod
    def injectDefaultConfig():
        if not isinstance(Config.configLib, dict):
            return False
        data = parseConfig(Config.yamlFile)
        Config.configLib = data

    @staticmethod
    def saveConfig():
        conformityConfig(Config.yamlFile, Config.configLib)

#全局变量类
class GlbLib:
    def __init__(self):
        self.MapLib = {}
    
    def get(self, key):
        return self.MapLib[key]
    
    def set(self, key, value):
        self.MapLib[key] = value
        return self.MapLib[key] == value

#文件操作类
class FileOp:
    def __init__(self):
        pass

#解析yaml文件
def parseConfig(yaml_file):
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data

def conformityConfig(yaml_file, data):
    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(data, file)
    file.close()

#判断当前程序是否在运行
def checkRunning():
    config = Config()
    now_pid = config.get("pid")
    pids = psutil.pids()
    if now_pid in pids:
        print("has progress running...")
        exit()
    now_pid = os.getpid()
    config.set("pid", now_pid)
    return now_pid

#操作文件类
#@Singleton
#class FileOp(object):
    
#目录结构
# -baseDir
# ---bin
# -----data.yaml
# ---version
# -----go
# -----python
# ---log
