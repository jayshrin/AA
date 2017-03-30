class emulator:
    resource_type = "emulator"
    def __init__(self,device_id,hub_id,user_id,platform,version,manufacturer,model):
        self.user_id = user_id #emulators should be created by admin, user is admin before assigned to any user
    	self.device_id = device_id
    	self.hub = hub_id
    	self.platform = platform # android or iOS
    	self.version = version
    	self.manufacturer = manufacturer
    	self.model = model
    	self.status = ""
        self.attached_hubs = [] # a list of attached hubs
        self.attached_emulators = [] # list of emulators
        self.allocation = False

    def get_resource(self,cpu_amt,memory_amt,storage_amt):
        #insert openstack sdk method here
        pass
        
    def release_resource(self):
        #insert openstack sdk method here
        pass
    
    def status(self):
        if self.user_id == "admin":
            return 0 #not assigned
        else:
            return 1 # assigned