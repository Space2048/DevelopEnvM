
#-*-coding:utf-8-*
import yaml

def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

#配置类
@Singleton
class Config(object):
    configLib = {}
    def __init__(self):
        self.injectDefaultConfig()

    @staticmethod
    def injectDefaultConfig():
        if (type(configLib) != "dict"):
            return False
        yamlFile = "../test/simple.yaml"
        data = parseConfig(yamlFile)
        configLib = data

    
    def get(self, name):
        return Config.configLib[name]

#全局变量类
@Singleton
class GlbLib(object):
    def __init__(self):
        self.MapLib = {}
    
    def get(self, key):
        return self.MapLib[key]
    
    def set(self, key, value):
        self.MapLib[key] = value
        return self.MapLib[key] == value

#文件操作类
@Singleton
class FileOp(object):
    def __init__(self):
        pass

def parseConfig(yaml_file):
    print("test")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


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
