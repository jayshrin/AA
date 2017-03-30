class hub:
    resource_type = "hub"
    def __init__(computer_id,device_list):
        self.computer_id = comuter_id
        self.device_list = device_list
        self.size = len(device_list) #indicate the number of mobile device or emulators connected
    
    def send_msg(device_no,command):
        result = device_list[device_no].computer_id.system(command) #function not completed
        return result;
        