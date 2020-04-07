#!/usr/bin/python3
""" test """
from fabric.api import local, settings, abort, run, put
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

def do_deploy(archive_path):
    env.hosts = ["34.73.26.158", "34.73.239.89"]
    noe = archive_path[9:-4]
    we = archive_path[9:]
    with settings(warn_only=True):
        try:
            if put(archive_path, '/tmp/').failed:
                return None
        except:
            return None
        if run("mkdir -p /data/web_static/releases/{}/".format(noe)).failed:
            return None
        if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                we, noe)).failed:
            return None
        if run("rm /tmp/{}".format(we)).failed:
            return None
        if run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(noe, noe)).failed:
            return None
        if run("rm -rf /data/web_static/releases/{}/web_static".format(
        we)).failed:
            return None
        if run("rm -rf /data/web_static/current").failed:
            return None
        if run("ln -s /data/web_static/releases/{}/ /data/web_static/cur\
        rent".format(we)).failed:
            return None
        return True
