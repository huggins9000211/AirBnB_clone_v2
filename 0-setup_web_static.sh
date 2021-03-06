#!/usr/bin/env bash
#test
place="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/hbnb_static/;\n\t}"
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo 'Hello World' > sudo /data/web_static/current/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "37i\ $place" /etc/nginx/sites-available/default
sudo service nginx restart
