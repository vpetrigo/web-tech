import multiprocessing

bind = "0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
