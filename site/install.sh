#!/usr/bin/env bash

sudo ln -s -f /home/box/web/site/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c etc/gu_config.py hello:app
# sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
