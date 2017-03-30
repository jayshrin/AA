from db_manip import DAO

db = DAO()
db.connect()
"""
print(db.get_clouds())
print(db.get_nodes(1))
print(db.get_vms(1,1))
print(db.get_node_freespace(1,1))
print(db.get_cloud_freespace(1))
"""

"""
from VMcontroller import VMcontroller
vc = VMcontroller()
print vc.create(10128742,"std_vm")
#vc.delete("VM1C2N1")
"""
from EMcontroller import EMcontroller
ec = EMcontroller()
#print ec.create(10128742,"Android",1,"std_emu")
ec.delete("EM1C2N1")

"""
class A:
	def printargs(args):
		print(args)
	printargs = staticmethod(printargs)

a=A()	
A.printargs("asdfasdf")
"""