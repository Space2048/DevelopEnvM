import time
import click
import os
from terminal_layout import *
from env_develop.utils import checkRunning
from env_develop.languagetools import py_toolbox

# 基本配置
# https://www.python.org/
# python 版本下载
# https://www.python.org/ftp/python/
# python list
def test():
    # pythont = py_toolbox()
    # list = pythont.getList()
    # for v in list:
    #     print(v)
    # pass
    checkRunning()
    


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
