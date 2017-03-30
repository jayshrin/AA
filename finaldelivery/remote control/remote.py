import sys
import os
address="10.189.158.134"
#address="192.168.1.77"
command = "sshpass -p stackstack ssh openstack@"+address+" 'nohup ./emulator.sh "+sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+"'"
os.system(command)
