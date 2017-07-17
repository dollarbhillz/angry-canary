from flask import Flask
from flask import request
import psutil
import time
import logging

app = Flask(__name__)

@app.route('/cpu')
def get_cpu_stats():
	return str(psutil.cpu_times())

@app.route('/memory')
def get_memory_stats():
	return str(psutil.virtual_memory())

@app.route('/disk')
def get_disk_io():
	return str(psutil.disk_usage())

@app.route('/log')
def start_log():
	logging.basicConfig(filename="specs.log", level=logging.INFO)
	print("writing to log")
	while(True):
		time.sleep(10)

		cpu_stat = "cpu_times: " + str(psutil.cpu_percent()) + "\n"
		memory_stats = "virtual_memory_stats: " + str(psutil.virtual_memory()) + "\n"
		disk_io = "disk_io: " + str(psutil.disk_usage()) + "\n"

		logging.info(cpu_stat)
		logging.info(memory_stats)
		logging.info(disk_io)

# if __name__ == '__main__':
# run(host='0.0.0.0', port=8080, debug=True)
