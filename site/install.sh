#!/usr/bin/env bash

# to simplify instalation configuring, provide your 'local_conf.sh'
# file that have to declare variables below:
### 
# > NGINX_SITE_ENABLE_PATH - path to the site-enable path of nginx
# > PROJECT_PATH - path to your project

if [[ ! -f local_conf.sh ]]; then
    echo "Provide local_conf.sh please"
    exit 1
fi

CURRENT_SYSTEM=`uname -s`

case $CURRENT_SYSTEM in
    FreeBSD)
        source init_scripts/bsd/system_scripts.sh
        ;;
    Linux)
        source init_scripts/linux/system_scripts.sh
        ;;
    *)
        echo "Your system is not supported yet"
        exit 1
esac

source local_conf.sh

update_pip()
{
    sudo pip3 install --upgrade pip setuptools
    sudo pip3 install gunicorn django
}

add_server_config()
{
    # move our server config to the nginx's site folder
    sudo ln -s -f $1/site/etc/nginx.conf $2
    sudo service nginx restart
}

system_update
update_pip
add_server_config $PROJECT_PATH $NGINX_SITE_ENABLE_PATH

# TODO do something with that shit
sudo gunicorn -c etc/gu_config.py hello:app &
cd ask
sudo gunicorn -c gu_config.py ask.wsgi &
