#!/usr/bin/python3
""" test """
from fabric.api import local, settings
import fabric
import datetime


def do_pack():
    """ test """
    try:
        dt = datetime.datetime.now()
        cname = "versions/web_static_{}{}{}{}{}.tgz".format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute
        )
        command = "tar -cvzf {} web_static".format(cname)
        with settings(warn_only=True):
            local("mkdir -p versions")
            result = local(command)
        if result.failed:
            return None
        return cname
    except Exception:
        return None
