import sys
import os

from os.path import expanduser
from subprocess import call

home = expanduser("~") #get home folder of the user
sudoPassword = '123456' #change to the real password here
android_sdk = 'android-sdk_r24.1.2-linux.tgz'

print home

android_sdk_dir = home+"/Android_SDK"

if not os.path.exists(android_sdk_dir):
    os.mkdir(android_sdk_dir)

os.chdir(android_sdk_dir)

command = 'sudo apt-get install openjdk-7-jdk -y'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

command = 'sudo apt-get install libgl1-mesa-dev:i386 -y'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))


call(["wget", "http://dl.google.com/android/"+android_sdk])
call(["tar", "-xvzf", android_sdk])

android_sdk_source = android_sdk_dir+"/android-sdk-linux"




