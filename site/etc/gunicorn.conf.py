# gunicorn configuration path for WSGI hello application

import multiprocessing

bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
user = "www"
group = "www"

umask = "0o77"
proc_name = "hello-app-server"

PARENT_DIR = os.path.abspath(__file__)
PROJECT_DIR = os.path.dirname(PARENT_DIR)

chdir = PROJECT_DIR
pidfile = "/var/run/" + proc_name + ".pid"

# logging
VAR_LOG = "/var/log/"
accesslog = VAR_LOG + proc_name + "/access.log"
errorlog = VAR_LOG + proc_name + "error.log"

