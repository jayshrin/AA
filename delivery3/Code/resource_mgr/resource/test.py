from cloud import cloud
from cloud import node
from resources.mobile import mobile

C1=cloud("C1","127.0.0.1")
print C1.capacity
N1 = node("C1N1","127.0.0.1",8,4096,500)
N2 = node("C1N2","127.0.0.2",16,4096,1000)
C1.add_node(N1)
print C1.capacity
C1.add_node(N2)
print C1.capacity

N1.create_vm("VM1","Linux",2,512,0)
print N1.get_usage()
print N2.get_usage()
print C1.get_usage()

ND = C1.node_list[0]
pad = mobile("mipad01","","admin","android","4.3.2","xiaomi","mipad")

ND.attach_mobile(pad)
N1.vm_list[0].new_emulator("mipad01","admin","android","4.3.2","xiaomi","mipad")

for nd in C1.node_list:
    print "node name: "+nd.name
    print "node capacity: "+str(nd.capacity)
    for vm in nd.vm_list:
        print "vm: "+vm.name
        for em in vm.hosted_emulators:
            print "emulator: "+em.device_id
    for mob in nd.mobile_list:
        print "phone: "+mob.device_id
         