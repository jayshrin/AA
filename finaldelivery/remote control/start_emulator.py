#to call this python script run python start_emulator <avd_name> <target_name> 
#example python start_emulator.py user_avd 1
import sys
import os

from os.path import expanduser
from subprocess import call

home = expanduser("~")
avd_name = sys.argv[1]
target_id=sys.argv[2]

android_sdk_dir = home+"/android-sdk-linux"
command = "echo no | " + android_sdk_dir+"/tools/android create avd -n "+avd_name+" -t "+target_id
print command
p = os.system(command)

command = android_sdk_dir+"/tools/emulator -avd "+avd_name+" -no-window"
#print command
p = os.system(command)

print p
