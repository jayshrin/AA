class least_used_allocator(allocator):
    def __init__(resource_type):
        self.resource_type = resource_type
        

	def process_request(self, request, clouds):
		free = {"cpu":0,"ram":0,"storage":0}
		best_match = clouds[0].node_list()[0]
        for cloud in clouds:
			for node in cloud:
				if node.get_free()>free
					best_match = node
		return node