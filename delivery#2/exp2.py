#!/usr/bin/env python
import time
import keystoneclient.v2_0.client as ksclient
import novaclient.client as nvclient
import glanceclient.v2.client as glclient

def get_nova_credentials_v2():
	d = {}
	d['version'] = '2'
	d['username'] = "demo"
	d['api_key'] = "stack"
	d['auth_url'] = "http://192.168.1.77:5000/v2.0"
	d['project_id'] = "demo"
	return d

try:
	credentials = get_nova_credentials_v2()
	keystone = ksclient.Client(auth_url="http://192.168.1.77:5000/v2.0",username = "admin",password = "stack",tenant_name="demo")

	glance_endpoint = keystone.service_catalog.url_for(service_type="image")
	glance = glclient.Client(glance_endpoint,token = keystone.auth_token)
	imgs = glance.images.list()
	for image in imgs:
		print(image.name)

	nova_client = nvclient.Client(**credentials)
	print(nova_client.servers.list())

	image = nova_client.images.find(name="cirros-0.3.2-x86_64-uec")
	flavor = nova_client.flavors.find(name="m1.tiny")
	net = nova_client.networks.find(label="private")
	nics = [{'net-id': net.id}]
	instance = nova_client.servers.create(name="vm2", image=image, flavor=flavor, nics=nics)
	print("Sleeping for 5s after create command")
	time.sleep(5)
	print("List of VMs")
	print(nova_client.servers.list())

	servers_list = nova_client.servers.list()
	server_del = "vm2"
	server_exists = False

	for s in servers_list:
		if s.name == server_del:
			print("This server %s exists" % server_del)
			server_exists = True
			break
	if not server_exists:
		print("server %s does not exist" % server_del)
	else:
		print("deleting server..........")
		nova_client.servers.delete(s)
		print("server %s deleted" % server_del)
finally:
	print("Execution Completed")
