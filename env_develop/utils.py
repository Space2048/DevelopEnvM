
#-*-coding:utf-8-*
from typing import Any
import yaml
import psutil
import os
import time
import platform
import requests
import sys
import time
from terminal_layout.extensions.progress import *

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


class BaseUtil(object):
    def __init__(self):
        pass

    #获取系统类型
    @staticmethod
    def get_system():
        return platform.system()

    @staticmethod
    def download_file(url, local_file):
        # 第一次请求是为了得到文件总大小
        requests.packages.urllib3.disable_warnings()
        r1 = requests.get(url, stream=True, verify=False)
        total_size = int(r1.headers['Content-Length'])

        # 这重要了，先看看本地文件下载了多少
        if os.path.exists(local_file):
            temp_size = os.path.getsize(local_file)  # 本地已经下载的文件大小
        else:
            temp_size = 0
        # 显示一下下载了多少   
        # print(temp_size)
        # print(total_size)
        # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
        headers = {'Range': 'bytes=%d-' % temp_size}  
        # 重新请求网址，加入新的请求头的
        r = requests.get(url, stream=True, verify=False, headers=headers)
        p = Progress("Downloading", total_size, unreached=".", reached="=")
        p.start()
        p.set_progress(temp_size)
        # 下面写入文件也要注意，看到"ab"了吗？
        # "ab"表示追加形式写入文件
        with open(local_file, "ab") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    temp_size += len(chunk)
                    f.write(chunk)
                    f.flush()
                    p.add_progress(len(chunk))
                    ###这是下载实现进度显示####

                    # done = int(50 * temp_size / total_size)
                    # sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                    # sys.stdout.flush()
        p.stop()
        print()  # 避免上面\r 回车符


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
        print("has progress running, exit...")
        exit()
    now_pid = os.getpid()
    config.set("pid", now_pid)
    Config.saveConfig()
    return now_pid

#软件初始化，创建基本环境
def softwareInit():
    config = Config()
    baseDir = config.get("download_dir")
    if not baseDir:
        baseDir = os.environ['HOME']
    baseDir = baseDir + "/.developEnvM"
    _isexist = os.path.exists(baseDir)
    if not _isexist:
        os.makedirs(baseDir)
    languages = config.get("languages")
    for lang in languages:
        langDir = baseDir + "/" + lang
        _isexist = os.path.exists(langDir)
        print(langDir)
        if not _isexist:
            os.mkdir(langDir)

 
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
