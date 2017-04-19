#!/usr/bin/env bash
# provide this script with:
# DB_NAME - database name to create
# DB_USER - user who will be granted with all privileges to ${DB_NAME} database
# DB_USER_PASSWD - new user's password

check_mysql_root() {
    # check whether it is possible to access MySQL
    # without password ... and with root :)
    mysql -u root &> /dev/null
    
    # yes, we definitely can
    [[ `echo $?` -eq 0 ]] && return 0
    
    return 1
}

service mysql status &> /dev/null

if [[ $? -ne 0 ]]; then
    echo "MySQL is not started. Launch it ..."
    service mysql start

    if [[ $? -ne 0 ]]; then
        echo "Cannot start MySQL service"
        
        exit $?
    fi
fi

if [[ -z check_mysql_root ]]; then
    MYSQL_CMD="mysql -u root"
else
    MYSQL_CMD="mysql -u root -p"
fi
# create DB and DB_User
# variables DB_NAME DB_USER and DB_USER_PASSWD must be set
$MYSQL_CMD -e "create database if not exists ${DB_NAME};"
$MYSQL_CMD -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'%' IDENTIFIED BY '${DB_USER_PASSWD}' WITH GRANT OPTION";

echo -e "[client]\ndatabase = ${DB_NAME}" > ask/ask/app.cnf
echo -e "user = ${DB_USER}\npassword = ${DB_USER_PASSWD}" >> ask/ask/app.cnf
