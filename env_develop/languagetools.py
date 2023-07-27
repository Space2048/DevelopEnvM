from utils import Config, GlbLib

class py_toolbox(object):
    
    def __init__(self):
        config = Config()
        self.version_url = config.get("pythonVersionUrl")
        self.download_url = config.get("pythonDowloadUrl")
        self.freshInfo()
        pass
    
    def freshInfo(self):
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
