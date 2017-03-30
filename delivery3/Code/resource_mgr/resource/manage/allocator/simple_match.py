class simple_match_allocator(allocator):
    def __init__(resource_type):
        self.resource_type = resource_type
		
    def simpleMatch(request):
        for cloud in clouds:
			for node in cloud:
				if isEnough(node,request):
					return node
		return None
	
	