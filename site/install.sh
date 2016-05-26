#!/usr/bin/env bash

# I would like to use python3 for that
update_pip() 
{
    sudo pip3 install --upgrade pip setuptools
    sudo pip install gunicorn django
}

# update current dist
system_update()
{
    sudo apt-get update -q
    sudo apt-get upgrade -yq
}

system_update
update_pip

# move our server config to the nginx's site folder
sudo ln -s -f /home/box/web/site/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo service nginx restart

sudo gunicorn -c etc/gu_config.py hello:app &
cd ask
sudo gunicorn -c gu_config.py ask.wsgi &
# sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
