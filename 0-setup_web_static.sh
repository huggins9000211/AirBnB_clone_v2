#!/usr/bin/env bash
#test
place="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/hbnb_static/\n\t}"
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo 'Hello World' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "37i\ $redirect" /etc/nginx/sites-available/default
