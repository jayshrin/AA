#!/usr/bin/env python
import time
import keystoneclient.v2_0.client as ksclient
import novaclient.client as nvclient
import glanceclient.v2.client as glclient

def get_nova_credentials_v2(): #get real user credentials from env or horizon
	d = {}
	d['version'] = '2'
	d['username'] = "demo"
	d['api_key'] = "stack"
	d['auth_url'] = "http://192.168.1.77:5000/v2.0"
	d['project_id'] = "demo"
	return d

def upload_ubuntu(path_to_ubuntu_img):
	admin_keystone = ksclient.Client(auth_url="http://192.168.1.77:5000/v2.0",username = "admin",password = "stack",tenant_name="demo")
	glance_endpoint = keystone.service_catalog.url_for(service_type="image")
	glance = glclient.Client(glance_endpoint,token = keystone.auth_token)
	imagefile = path_to_ubuntu_img
	with open(imagefile) as fimage:
		glance.images.create(name="ubuntu", is_public=True, disk_format="qcow2",container_format="bare", data=fimage)

def start_ubuntu():
	credentials = get_nova_credentials_v2()
	nova_client = nvclient.Client(**credentials)

	user_keystone = ksclient.Client(auth_url="http://192.168.1.77:5000/v2.0",username = "demo",password = "stack",tenant_name="demo")
	glance_endpoint = keystone.service_catalog.url_for(service_type="image")
	glance = glclient.Client(glance_endpoint,token = keystone.auth_token)
	imgs = glance.images.list()
	has_ubuntu=False
	for image in imgs:
		print(image.name)
		if name == "ubuntu"
			has_ubuntu=True
	if has_ubuntu ==False
		upload_ubuntu("~/Downloads/trusty-server-cloudimg-amd64-disk1.img")
	
	print(nova_client.servers.list())
	image = nova_client.images.find(name="ubuntu")
	flavor = nova_client.flavors.find(name="m1.tiny")
	net = nova_client.networks.find(label="private")
	nics = [{'net-id': net.id}]
	instance = nova_client.servers.create(name="vm2", image=image, flavor=flavor, nics=nics)
	print("List of VMs")
	print(nova_client.servers.list())

def terminate_ubuntu():
	credentials = get_nova_credentials_v2()
	nova_client = nvclient.Client(**credentials)
	servers_list = nova_client.servers.list()
	server_del = "ubuntu"
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
	print("List of VMs")
		print(nova_client.servers.list())
