cloud_list[]
user_list[]

LB = LoadBalancer()
request = NewRequest()
chosen_node = LB(request)
chosen_node.allocate_resource_for(request)
