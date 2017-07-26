from flask import Flask
from flask import request
import os
import psutil
import time
import logging

app = Flask(__name__)


# Returns cpu metrics.
@app.route('/cpu')
def get_cpu_stats():
    return str(psutil.cpu_times()) + '\n'


# Returns memory metrics.
@app.route('/memory')
def get_memory_stats():
    return str(psutil.virtual_memory()) + '\n'


# Returns disk metrics
# Warning: This does not currently work when within a container and will return
# an internal server error
@app.route('/disk')
def get_disk_io():
    return str(psutil.disk_usage()) + '\n'


# Writes cpu, and memory metrics to a log file every 10ms. Currently, disk
# metrics are commented out because they will not work when within a container.
# This should maybe be another child process?
@app.route('/log')
def start_log():
    logging.basicConfig(filename="health.log", level=logging.INFO)
    while(True):
        time.sleep(10)

        cpu_stats = "cpu_stats: " + str(psutil.cpu_percent()) + "\n"
        memory_stats = "memory_stats: " + str(psutil.virtual_memory()) + "\n"
       # disk_stats = "disk_io: " + str(psutil.disk_usage()) + "\n"

        logging.info(cpu_stat)
        logging.info(memory_stats)
       # logging.info(disk_io)


# begin simulating work
@app.route('/busy_work/<workers>')
def busy_work(workers):
    #process = os.popen("python busy_work.py", 'w', 1)
    #process.write(workers + '\n')
    return "currently " + workers + " workers running"


if __name__ == "__main__":
    process = os.popen("python busy_work.py", 'w', 1)
    process.write("1\n")
    app.run(host='127.0.0.1')
