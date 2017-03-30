from resources.computer import computer
from resources.mobile import mobile
class cloud:
    """
    instances of this cloud class should be created after a new cluster is joined to the MIaaS Cloud
    """
    def __init__(self,name,ip,internal = True):
        self.name = name
        self.ip = ip
        self.node_list = [] #no node when 
        #define the maximum capacity of this cloud
        self.capacity = {}
        self.capacity["cpu"] = 0
        self.capacity["ram"] = 0
        self.capacity["storage"] = 0
        self.internal = internal
        
    def add_node(self,new_node):
        self.node_list.append(new_node)
        self.capacity["cpu"]+=new_node.capacity["cpu"]
        self.capacity["ram"]+=new_node.capacity["ram"]
        self.capacity["storage"]+=new_node.capacity["storage"]
    
    def get_usage(self):
        usage = {"cpu":0,"ram":0,"storage":0}
        for node in self.node_list:
            usg = node.get_usage()
            usage["cpu"]+=usg["cpu"]
            usage["ram"]+=usg["ram"]
            usage["storage"]+=usg["storage"]
        return usage
        
        
class node:
    """
    instances of this node class should be created after a new node is joined to the MIaaS Cloud
    """
    def __init__(self,name,ip,cpu_cap,ram_cap,storage_cap):
        self.name = name
        self.ip = ip
        self.capacity = {}
        self.capacity["cpu"] = cpu_cap
        self.capacity["ram"] = ram_cap
        self.capacity["storage"] = storage_cap
        self.vm_list = []
        self.mobile_list = []
    
    def attach_mobile(self,phone):
        self.mobile_list.append(phone)
    
    def get_usage(self):
        usage = {"cpu":0,"ram":0,"storage":0}
        for vm in self.vm_list:
            usage["cpu"]+=vm.cpu_amt
            usage["ram"]+=vm.ram_amt
            usage["storage"]+=vm.storage_amt
        return usage
    
    def create_vm(self,name,os,cpu_amt,ram_amt,storage_amt):
        if cpu_amt > self.capacity["cpu"]:
            print "cannot create vm, out of CPU capacity"
            return 0
        if ram_amt > self.capacity["ram"]:
            print "cannot create vm, out of RAM capacity"
            return 0
        if storage_amt > self.capacity["storage"]:
            print "cannot create vm, out of storage capacity"
            return 0
        
        new_vm = computer(name,os,cpu_amt,ram_amt,storage_amt,host_node=self)
        self.vm_list.append(new_vm)
        #new_vm.get_resource()
        return 1
        
    def find_vm(self,name):
        for vm in self.vm_list:
            if vm.name == name:
                return vm
        print "vm not found"
        return None
        
    def delete_vm(self,vm_name):
        vm = self.find_vm(vm_name)
        if vm is None:
            print "unknown vm"
            return
        else:
            vm.release_resource()
            vm_list.remove(vm)
        
        
        
        
        