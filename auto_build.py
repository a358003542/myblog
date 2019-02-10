#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import glob
import os
import sys
import click
PROJECT = 'myblog'
publish_path = "publish"

devbuild_path = "output"


@click.group()
def main():
    pass


@main.command()
def devbuild():
    """
    build your pelican project
    """
    click.echo("start devbuild your pelican project...")

    click.echo('right now you are in folder: {0}'.format(os.getcwd()))

    cmd = "pelican content -o {devbuild_path} -s .\pelicanconf.py".format(
        devbuild_path=devbuild_path)

    click.echo('start run cmd: {0}'.format(cmd))
    ret = subprocess.call(cmd)

    click.echo('running result is:{0}'.format(ret))


@main.command()
def devserve():
    """
    devserve you publish output
    """
    
    
    cmd = 'start_server.bat'
    

    click.echo('serve on : http://localhost:8000')
    ret = subprocess.run(cmd)
   
    click.echo('running result is:{0}'.format(ret))

   

@main.command()
def devclean():
    """
    clean your dev output
    """

    cmd = 'rm -rf output/*'
    ret = subprocess.call(cmd)
    click.echo('running result is:{0}'.format(ret))
    
@main.command()
def devserve_stop():
    """
    devserve you publish output
    """
    cmd = 'bash ./develop_server.sh stop'
    click.echo('serve on : http://localhost:8000')
    ret = subprocess.call(cmd)
    click.echo('running result is:{0}'.format(ret))


@main.command()
def build():
    """
    build your pelican project
    """
    click.echo("start build your pelican project...")

    click.echo('right now you are in folder: {0}'.format(os.getcwd()))

    cmd = "pelican content -o {publish_path} -s .\publishconf.py".format(
        publish_path=publish_path)

    click.echo('start run cmd: {0}'.format(cmd))
    ret = subprocess.call(cmd)

    click.echo('running result is:{0}'.format(ret))




if __name__ == '__main__':
    main()
