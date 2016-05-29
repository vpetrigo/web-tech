# system dependent function definitions

system_update()
{
    if [[ ! -z `command -v lsb_version` ]]; then
        sudo apt-get update -q
        sudo apt-get upgrade -qy
    else
        echo "Nothing to do"
    fi
}

start_app_servers()
{
    RUNIT_DIR="$1/init_scripts/runit"
    apps=(ask_app hello_app)

    for app in ${apps[*]}; do
        echo "GUNICORN_EXEC=gunicorn" >> $RUNIT_DIR/${app}/local_vars
    done

    echo "GUNICORN_ARGS='-c $1/etc/gunicorn.conf.py hello:app'" >> $RUNIT_DIR/hello_app/local_vars
    echo "GUNICORN_ARGS='-c $1/ask/gunicorn.conf.py ask.wsgi'" >> $RUNIT_DIR/ask_app/local_vars

    sudo ln -s -f $RUNIT_DIR/hello_app /etc/service/
    sudo ln -s -f $RUNIT_DIR/ask_app /etc/service/
}
