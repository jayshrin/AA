import sys
import os

from os.path import expanduser
from subprocess import call

home = expanduser("~")
sudoPassword = '123456' # change to real password here
avd_name ='cloud_avd'

target_id='android-8'
abi_name='default/armeabi-v7a'

print home

android_sdk_dir = home+"/android"

os.chdir(android_sdk_dir)

android_sdk_source = android_sdk_dir+"/android-sdk-linux"

#command = 'sudo apt-get install openjdk-7-jdk -y'
#p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

command = "echo no | " + android_sdk_source+"/tools/android create avd -n "+avd_name+" -t "+target_id
print command
p = os.system(command)

command = android_sdk_source+"/tools/emulator -avd "+avd_name

print command
p = os.system(command)

