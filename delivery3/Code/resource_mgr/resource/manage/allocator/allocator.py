class allocator:
	def _is_matched(self, node, request):
		usg = node.get_usage()
		if node.capacity["cpu"]-use["cpu"] < request.cpu:
			return False
		if node.capacity["ram"]-use["ram"] < request.cpu:
			return False
		if node.capacity["storage"]-use["storage"] < request.cpu:
			return False
		return True
    