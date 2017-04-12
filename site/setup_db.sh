#!/usr/bin/env bash

service mysql status &> /dev/null

if [[ $? -ne 0 ]]; then
    echo "MySQL is not started. Launch it ..."
    service mysql start

    if [[ $? -ne 0 ]]; then
        echo "Cannot start MySQL service"
        
        exit $?
    fi
fi
# create DB and DB_User
# variables DB_NAME DB_USER and DB_USER_PASSWD must be set

mysql -u root -p -e "create database if not exists ${DB_NAME};"
mysql -u root -p -e "create user if not exists '${DB_USER}'@'%' identified by '${DB_USER_PASSWD}';"
mysql -u root -p -e "grant all privileges on ${DB_NAME}.* to '${DB_USER}'@'%';"
