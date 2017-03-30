1. put emulator.sh, start_emulator.py and stop_emulator file under the home folder of openstack server node
2. put remote.py in the webserver
3. configure the ip address in remote.py
4. run remote.py
	python remote.py <start/stop> <avd_name> <target>
	eg: 
		python remote.py start remote_avd 1
		python remote.py stop remote_avd emulator-5554
