# update current dist
system_update()
{
    sudo apt-get update -q
    sudo apt-get upgrade -yq
}

start_app_servers()
{
    sudo service hello_app start GUNICORN_CONF_PATH=$1
    sudo service ask_app start GUNICORN_CONF_PATH=$1
}
