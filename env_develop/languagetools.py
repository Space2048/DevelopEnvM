from env_develop.utils import Config, BaseUtil
import requests
from bs4 import BeautifulSoup

def createToolBox(typ):
    toolType = {"python":py_toolbox,"go":go_toolbox}
    if typ not in toolType.keys():
        return None
    return toolType[typ]()

class py_toolbox(object):
    
    def __init__(self):
        config = Config()
        self.version_url = config.get("python_version_url")
        self.download_url = config.get("python_download_url")
        self.local_version = config.get("python_local_version")
        self.platform = BaseUtil.get_system()
        self.freshInfo()
        pass
    
    def freshInfo(self):
        self.versionList = py_toolbox._request_version(self.version_url)
        self.saveData("python_version_list", self.versionList)
        pass

    def getList(self):
        return self.versionList
    
    def install(self, version):
        
        pass

    def download(self, version):
        if version not in self.versionList:
            return ""
        else:
            packName = self.getPackageName(version)
            print(packName)
            pass
    
    def getPackageName(self, version):
        packName = ""
        if self.platform == "Linux":
            packName = "Python-" + version + ".tar.xz"
        return packName

    def makeVersion(self, file):
        
        pass

    def saveData(self, key, value):
        config = Config()
        config.set(key, value)
        config.saveConfig()
        pass
    
    @staticmethod
    def _request_version(url) -> str:
        response = requests.get(url, timeout= 10)
        h5 = response.content
        soup = BeautifulSoup(h5, 'lxml')
        data = soup.findAll("a")
        list = []
        for el in data:
            version = str(el.string)
            version = version.replace("/", "")
            list.append(version)
        return list[1:-18]

    @staticmethod
    def _request_download(url, dir) -> str:
        BaseUtil.download_file(url, dir)

class go_toolbox(object):
    def __init__(self) -> None:
        pass

