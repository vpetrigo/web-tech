# system dependent function definitions

system_update()
{
    echo "BSD. Nothing to do"
}

start_app_servers()
{
    sudo service hello_app start $1
    sudo service ask_app start $1
}
