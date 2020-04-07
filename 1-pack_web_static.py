#!/usr/bin/python3
""" test """
from fabric.api import local, settings, abort
import fabric
import datetime


def do_pack():
    """ test """
    dt = datetime.datetime.now()
    cname = "versions/web_static_{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute
    )
    command = "tar -cvzf {} web_static".format(cname)
    print("Packing web_static to {}".format(cname))
    with settings(warn_only=True):
        local("mkdir -p versions")
        result = local(command)
    if result.failed or result.return_code != 0:
        return None
    return "AirBnB_clone_v2/web_static/{}".format(cname)
