#!/usr/bin/env bash
##################################################################################
# to simplify instalation process, provide your 'local_conf.sh'
# file that has to declare variables below:
################################################################################## 
# > NGINX_SITE_ENABLE_PATH - path to the site-enable path of nginx
# > SERVER_NGINX_CONF_PATH - path to your nginx configuration. 
# example: '/home/<user>/web/etc/nginx.conf'; '/var/www/site/conf/site.conf'
###
# > HELLO_APP_RUN_SERVER_SCRIPT - path to the gunicorn.conf.py of the Hello app
# > ASK_APP_RUN_SERVER_SCRIPT - path to the gunicorn.conf.py of the Ask app

if [[ ! -f local_conf.sh ]]; then
    echo "Provide local_conf.sh please"
    exit 1
fi

CURRENT_SYSTEM=`uname -s`

# select initial scripts according to the OS type
case $CURRENT_SYSTEM in
    FreeBSD)
        source init_scripts/bsd/system_scripts.sh
        ;;
    Linux)
        source init_scripts/runit/system_scripts.sh
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
    sudo ln -s -f $1 $2
    sudo service nginx restart
}

add_gunicorn_app_server()
{   
    sudo cp $1 $2
}

# have to be defined in the system init_script 'system_scripts.sh'
system_update

update_pip
add_server_config $SERVER_NGINX_CONFIG_PATH $NGINX_SITE_ENABLE_PATH

# Add Hello application server
add_gunicorn_app_server $HELLO_APP_RUN_SERVER_SCRIPT $GUNICORN_APPS_PATH
# Add Ask application server
add_gunicorn_app_server $ASK_APP_RUN_SERVER_SCRIPT $GUNICORN_APPS_PATH 

start_app_servers `pwd`
