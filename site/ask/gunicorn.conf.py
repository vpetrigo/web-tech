# gunicorn Ask application server config

import multiprocessing
import os.path

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

user = "nobody"
group = "nogroup"

proc_name = "ask_app-server"
# set umask (in Python 3.5 077 with base 0 is not valid)
# so 0o prefix must be used
umask = "0o77"

PARENT_DIR = os.path.abspath(__file__)
PROJECT_DIR = os.path.dirname(PARENT_DIR)

chdir = PROJECT_DIR
#pidfile = "/var/run/" + proc_name + ".pid"

# logging
#VAR_LOG = "/var/log/"
#accesslog = VAR_LOG + proc_name + "/access.log"
#errorlog = VAR_LOG + proc_name + "/error.log"
