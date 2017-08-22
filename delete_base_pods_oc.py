# Delete le pods script
import os

os.system("oc get pods > pods.txt")
pods = open("pods.txt", 'r')

for lines in pods:
    line = lines.split()
    if "base-" in line[0]:
        os.system("oc delete pod " + line[0])

pods.close()

os.system("rm pods.txt")
