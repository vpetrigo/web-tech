import multiprocessing
import os

bind = "0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

user = "www"
group = "www"
proc_name = "ask_app"
# set umask (in Python 3.5 077 with base 0 is not valid)
# so 0o prefix must be used
umask = "0o77"

chdir = "/home/vpetrigo/projects/web-tech/site/ask"
