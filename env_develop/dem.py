from utils import Config

class VersionPageInfo(object):

    def __init__(self, typ):
        self.typ = typ

    def getParseMachine(self):
        config = Config()
        if self.typ == "python":
            pass


