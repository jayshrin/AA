import sys
from EMcontroller import EMcontroller
from VMcontroller import VMcontroller

if __name__ == "__main__":
	operation = sys.argv[1] #create/delete
	resource = sys.argv[2] #vm/emu/mobile
	user = int(sys.argv[3])	#user id
	
	
	if operation == "create":
		if resource == "vm":
			flavor = sys.argv[4]
			vm_ctrl = VMcontroller()
			vm_name = vm_ctrl.create(user,flavor)
			if vm_name is not None:
				print vm_name
			else:
				print "Error! Unable to create vm"

			
		elif resource == "emulator":
			#10128742,"Android",1,"std_emu"
			em_ctrl = EMcontroller()
			pltfm = sys.argv[4]
			target = int(sys.argv[5])
			flavor = sys.argv[6]
			em_name = em_ctrl.create(user,pltfm,target,flavor)
			if em_name is not None:
				print em_name

			else:
				print "Error! Unable to create vm"

				
		elif resource == "mobile":
			"""should add model options here"""
			mob_id = em_ctrl.create(user)
		else:
			print("unknown resource type")
	elif operation == "delete":
		device = sys.argv[4] #device id
		if resource == "vm":
			vm_ctrl = VMcontroller()
			if vm_ctrl.delete(device) == 1:
				print "success"
			
			else:
				print "Error"
				
	
		elif resource == "emulator":
			em_ctrl = EMcontroller()
			if em_ctrl.delete(device)==1:
				print "success"
				
			else:
				print "Error"
				
		elif resource == "mobile":
			mob_id = em_ctrl.delete(user,device)
		else:
			print("unknown resource type")