import time
import click
import os
from terminal_layout import *
from env_develop.utils import Config

# 基本配置
# https://www.python.org/
# python 版本下载
# https://www.python.org/ftp/python/
# python list


def interaction_mode():
    config = Config()
    print("interaction_mode")
    print(config.get("languages"))
    print("__________________")
    pass

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
