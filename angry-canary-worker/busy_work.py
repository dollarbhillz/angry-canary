import os
import psutil
import sys

class BusyWorker:
    def __init__(self):
        self.child_id = 0 # Pid of the child process which calls stress

    # Create n processes doing busy work by running the stress command
    def create_processes(self, num_children):

        print(num_children)

        # If stress children already exist, kill them before making more
        if self.child_id != 0:
            p = psutil.Process(self.child_id)
            p.terminate()


        # Create appropriate number of child processes
        pid = os.fork()

        if(pid == 0):
            os.execlp("stress", "-c", "--cpu", num_children.rstrip())
        else:
            self.child_id = pid


if __name__=="__main__":

    worker = BusyWorker()
    worker.create_processes("2")
    # Wait for input from parent process server.py
    # When input is recieved create the appropriate number of stress workers
    #while True:
    #    numProcesses = sys.stdin.readline()
    #
    #    if(numProcesses != ""):
    #        worker.create_processes(numProcesses)
