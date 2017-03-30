from resources.emulator import emulator
class computer:
    resource_type = "computer"
    def __init__(self,name,os,cpu_amt,ram_amt,storage_amt,host_node):
        self.private_ip = ""
        self.public_ip = ""
        self.name = name
        self.host_node = host_node # define which node it belongs to
        self.os = os # OS in ("Windows","Linux")
        self.cpu_amt = cpu_amt # define the number of vcpus
        self.ram_amt = ram_amt
        self.storage_amt = storage_amt
        self.attached_hubs = [] # a list of attached hubs, to get mobile device info, visit hubs
        self.hosted_emulators = []
        self.status = "preallocation"
    
    def get_resource(self,cpu_amt,memory_amt,storage_amt):
        #insert openstack sdk method here
        self.status = "allocated"
        
    def release_resource(self):
        #insert openstack sdk method here
        self.status = "released"
        
    def new_emulator(self,device_id,user_id,platform,version,manufacturer,model):
        new_em = emulator(device_id,"",user_id,platform,version,manufacturer,model)
        self.hosted_emulators.append(new_em)
    