from flask import Flask
from flask import request
import os
import psutil
import time
import logging

app = Flask(__name__)


# grab psutil cpu usage metrics
@app.route('/cpu')
def get_cpu_stats():
    return str(psutil.cpu_times()) + '\n'



# grab psutil memory metrics 
@app.route('/memory')
def get_memory_stats():
    return str(psutil.virtual_memory()) + '\n'



# grab psutil disk metrics 
# warning: does not currently work when within a container
# will return an internal server error 
@app.route('/disk')
def get_disk_io():
    return str(psutil.disk_usage()) + '\n'


# begin writing to log every 10 seconds 
@app.route('/log')
def start_log():
    logging.basicConfig(filename="health.log", level=logging.INFO)
    print("writing to log")
    while(True):
        time.sleep(10)

        cpu_stat = "cpu_times: " + str(psutil.cpu_percent()) + "\n"
        memory_stats = "virtual_memory_stats: " + str(psutil.virtual_memory()) + "\n"
        #disk_io = "disk_io: " + str(psutil.disk_usage()) + "\n"

        logging.info(cpu_stat)
        logging.info(memory_stats)
        #logging.info(disk_io)


# begin simulating work
@app.route('/busy_work')
def busy_work():
    os.system('stress -c 1&')
    return "stress currently at 1 process"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
