#!/bin/bash
py_dir="~/Documents/controllers"
operation=$1
estart="start"
estop="stop" 
if [ "$operation" == "$estart" ]; then
	avd_name=$2
	target_name=$3
	echo `python start_emulator.py $avd_name $target_name`
elif [ "$operation" == "$estop" ]; then
	avd_name=$2
	emulator_name=$3
	echo `python stop_emulator.py $avd_name $emulator_name`
fi

