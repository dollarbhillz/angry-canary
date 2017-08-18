from flask import Flask

from flask import request
import os
import psutil
import time
import logging
from hawkular.metrics import HawkularMetricsClient, MetricType


app = Flask(__name__)

#Create client object
client = HawkularMetricsClient(tenant_id='test')

# Get cpu metrics.
#@app.route('/cpu')
#def get_cpu_stats():
cpu_percent = psutil.cpu_percent(interval = 1, percpu = True)
for index, cpu in enumerate(cpu_percent) :
    client.create_metric_definition(MetricType.Gauge, 'cpu%s' % index, cpu = 'cpu%s' % index)

# Get memory metrics.
#@app.route('/memory')
#def get_memory_stats():
#    return str(psutil.virtual_memory()) + '\n'


# Get disk metrics
# Warning: This does not currently work when within a container and will return
# an internal server error
#@app.route('/disk')
#def get_disk_io():
#    return str(psutil.disk_usage()) + '\n'

#Return all metrics
while True :
    cpu_percent = psutil.cpu_percent(interval = 1, percpu = True)
    for index, cpu in enumerate(cpu_percent) :
        client.push(MetricType.Gauge, 'cpu%s'% index, float(cpu))


# Simulate work being done and then return
#@app.route('/do_work')
#def do_work():
#    fib(35)

#    return "work finished"

# Recursively computes Fibonacci numbers for the sake of fake work
#def fib(n):
#    if n <= 1:
#        return n
#    else:


if __name__ == "__main__":
    app.run(host='0.0.0.0')
