from env_develop.utils import Config
import requests
from bs4 import BeautifulSoup

class py_toolbox(object):
    
    def __init__(self):
        config = Config()
        self.version_url = config.get("python_version_url")
        self.download_url = config.get("python_download_url")
        self.local_version = config.get("python_loacl_version")
        self.freshInfo()
        pass
    
    def freshInfo(self):
        self.versionList = py_toolbox._request_version(self.version_url)
        pass

    def getList(self):
        return self.versionList
    
    def install(self, version):
        if version not in self.versionList:
            return ""
        else:
            pass

    def saveData(self, key, value):
        pass
    
    @staticmethod
    def _request_version(url) -> str:
        response = requests.get(url, timeout= 10)
        #response = ""
        # try:
        #     response = requests.get(url, timeout= 10)
        # except BaseException:
        #     print("network error")
        #     exit()
        h5 = response.content
        soup = BeautifulSoup(h5, 'lxml')
        data = soup.findAll("a")
        list = []
        for el in data:
            version = str(el.string)
            version = version.replace("/", "")
            list.append(version)
        return list[1:-18]
        
        # h5 = h5.replace("</a>", "|")
        #data = h5
        #soup.findAll(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
        # print(type(data))
        # print(data)