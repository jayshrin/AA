#to call this python script run python stop_emulator <avd_name> <emu_name> 
#example python stop_emulator user_avd emulator-5554
import sys
import os

from os.path import expanduser
from subprocess import call

home = expanduser("~")
#sudoPassword = '123456' # change to real password here
avd_name = sys.argv[1]
emu_name = sys.argv[2]

print home

android_sdk_dir = home+"/android-sdk-linux"


command = android_sdk_dir+"/platform-tools/adb -s "+emu_name+" emu kill"

print command
p = os.system(command)


command = "echo no | " + android_sdk_dir+"/tools/android delete avd -n "+avd_name
print command
p = os.system(command)

"""
"""
