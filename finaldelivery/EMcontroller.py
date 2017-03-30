from db_manip import DAO

class EMcontroller:
	name = "VMcontroller"
	def __init__(self):
		self.db = DAO()
		self.db.connect()
		
	
		
	def matchNode(self,flavor):
		flv = self.db.get_flavor(flavor)
		
		cloud_list = []
		node_list = []
		cd = self.db.get_clouds()
		for i in cd:
			cloud_list.append(i[0])

		free_space=[]
		for c in cloud_list:
			nodes = self.db.get_nodes(c)
			for node in nodes:
				node_list.append([c,node[1]])
				free_space.append(self.db.get_node_freespace(c,node[1]))
		#print node_list

		#print free_space
		for i in range(len(node_list)):
			for j in range(3):
				free_space[i][j] = free_space[i][j]/flv[j]
		
		#print free_space
		shortest_match=[]
		for fit in free_space:
			shortest_match.append(min(fit))

		buf_max = max(shortest_match)
		for i in range(len(shortest_match)):
			if shortest_match[i] == buf_max:
				best_match = node_list[i]
		#print best_match
		return best_match
		

	
	def create(self,user_id,platform,target,flavor):
		node = self.matchNode(flavor)
		#make a system call here
		name = self.db.add_em_info(node[0],node[1],user_id,platform,target,flavor)
		return name
		
	def delete(self,em_id):
		res = self.db.del_em_info(em_id)
		#make a system call here
		return res