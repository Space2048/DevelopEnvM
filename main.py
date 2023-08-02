import time
import click
import os
from terminal_layout import *
from terminal_layout.extensions.progress import *
from env_develop.utils import checkRunning, softwareInit, BaseUtil, SingletonMeta, DEMLog
from env_develop.languagetools import createToolBox


class DevelopEnvManager(metaclass = SingletonMeta):
    def __init__(self):
        self.langTools = {}
        pass
    def init(self):
        pass
    def version(self, typ):
        pass
    def install(self, typ):
        pass
    def changeVersion(self, typ):
        pass

def get_DevEnvManager():
    return DevelopEnvManager()

# 基本配置
# https://www.python.org/
# python 版本下载
# https://www.python.org/ftp/python/
# python list
def test():
    logger = DEMLog()
    logger.info("test")
    logger.warning("adx", "dasd")
    # softwareInit()
    #BaseUtil.download_file("https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tar.xz", "./Python-3.7.10.tar.xz")
    # p = Progress('Downloading', 100)
    # p.start()
    # #p.set_progress(2)
    # time.sleep(0.3)
    # for i in range(100):
    #     if p.is_finished():
    #         break
    #     time.sleep(0.3)
    #     p.add_progress(1)
    # p.stop()
    # pythont = py_toolbox()
    # res = pythont.download("3.7.10")
    # print(res)
    # list = pythont.getList()
    # for v in list:
    #     print(v)
    # pass
    # checkRunning()
    


def interaction_mode():
    test()

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        interaction_mode()


@cli.command()
@click.argument("typ", nargs = 1)
@click.argument("option", nargs = 1)
def list(typ, option):
    print("python2.7.0")
    print(typ)
    print(option)


if __name__ == '__main__':

    cli()
