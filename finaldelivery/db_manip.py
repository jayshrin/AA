import mysql.connector as db

class DAO:
	def __init__(self):
		self.active = False
	
	def connect(self):
		self.cnx=db.connect(user='root',database='MIAAS')
		self.active = True
		
	def close(self):
		self.cnx.close()
		self.active = False
		
	def get_clouds(self):
		try:
			cur = self.cnx.cursor()
			query = "SELECT * FROM clouds"
			cur.execute(query)
			result = cur.fetchall()
			cur.close()
			return result
		except db.Error as err:
			print("something went wrong"%err)
			return None
			
	def get_nodes(self,cloud_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT * FROM nodes WHERE cloud_id = %d"%(cloud_id)
			cur.execute(query)
			result = cur.fetchall()
			cur.close()
			return result
		except db.Error as err:
			print("something went wrong"%err)
			return None
			
	def get_vms(self,cloud_id,node_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT * FROM vms WHERE cloud_id = %d AND node_id = %d AND active = 1"%(cloud_id,node_id)
			cur.execute(query)
			result = cur.fetchall()
			cur.close()
			return result
		except db.Error as err:
			print("something went wrong"%err)
			return None
	
	def get_ems(self,cloud_id,node_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT * FROM emulators WHERE cloud_id = %d AND node_id = %d AND active = 1"%(cloud_id,node_id)
			cur.execute(query)
			result = cur.fetchall()
			cur.close()
			return result
		except db.Error as err:
			print("something went wrong"%err)
			return None
	
	def get_node_freespace(self,cloud_id,node_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT cpu,ram,storage FROM vms WHERE cloud_id = %d AND node_id = %d AND active = 1"%(cloud_id,node_id)
			cur.execute(query)
			vmusage = cur.fetchall()
			
			query = "SELECT cpu,ram,storage FROM emulators WHERE cloud_id = %d AND node_id = %d AND active = 1"%(cloud_id,node_id)
			cur.execute(query)
			emusage = cur.fetchall()
			
			#print usage
			query2 = "SELECT cpu_cap,ram_cap,storage_cap FROM nodes WHERE cloud_id = %d AND node_id = %d"%(cloud_id,node_id)
			cur.execute(query2)
			cap = cur.fetchone()
			#print cap
			cur.close()
			free=[cap[0],cap[1],cap[2]]
			for u in vmusage:
				for i in range(3):
					free[i]-=u[i]
			for u in emusage:
				for i in range(3):
					free[i]-=u[i]
			return free
		except db.Error as err:
			print("something went wrong %s"%err)
			return None
		
	def get_cloud_freespace(self,cloud_id):
		cur = self.cnx.cursor()
		query = "SELECT node_id FROM nodes WHERE cloud_id = %d"%(cloud_id)
		cur.execute(query)
		nd = cur.fetchall()
		cur.close()
		free = [0,0,0]
		#print nd
		for n in nd:
			fs = self.get_node_freespace(cloud_id,n[0])
			for i in range(3):
				free[i]+=fs[i]
		#print free
		return free
		
	def add_vm_info(self,cloud_id,node_id,user_id,flavor):
		flv = self.get_flavor(flavor)
		try:
			cur = self.cnx.cursor()
			query = "SELECT COUNT(*) FROM vms WHERE cloud_id = %d AND node_id = %d"%(cloud_id,node_id)
			cur.execute(query)
			vm_nb = cur.fetchone()[0]
			name = "VM"+str(vm_nb+1)+"C"+str(cloud_id)+"N"+str(node_id)
			query = "INSERT INTO vms VALUES(%d,%d,\'%s\',%d,%d,%d,1)"%(cloud_id,node_id,name,flv[0],flv[1],flv[2])
			cur.execute(query)
			self.cnx.commit()
			query = "INSERT INTO vm_usage VALUES(%d,\'%s\',CURTIME(),NULL)"%(user_id,name)
			cur.execute(query)
			self.cnx.commit()
			cur.close()
			return name
		except db.Error as err:
			print("something went wrong: %s"%err)
			return 0
	
	def add_em_info(self,cloud_id,node_id,user_id,platform,target,flavor):
		flv = self.get_flavor(flavor)
		try:
			cur = self.cnx.cursor()
			query = "SELECT COUNT(*) FROM emulators WHERE cloud_id = %d AND node_id = %d"%(cloud_id,node_id)
			cur.execute(query)
			em_nb = cur.fetchone()[0]
			name = "EM"+str(em_nb+1)+"C"+str(cloud_id)+"N"+str(node_id)
			query = "INSERT INTO emulators VALUES(%d,%d,\'%s\',\'%s\',\'%s\',%d,%d,%f,1)"%(cloud_id,node_id,name,platform,target,flv[0],flv[1],flv[2])
			cur.execute(query)
			self.cnx.commit()
			query = "INSERT INTO em_usage VALUES(%d,\'%s\',CURTIME(),NULL)"%(user_id,name)
			cur.execute(query)
			self.cnx.commit()
			cur.close()
			return name
		except db.Error as err:
			print("something went wrong: %s"%err)
			return 0
	
	def del_vm_info(self,vm_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT * FROM vms WHERE vm_id = \'%s\' AND active = 1"%(vm_id)
			cur.execute(query)
			if cur.fetchone()is None:
				return 0
			query = "UPDATE vms SET active = 0 WHERE vm_id = \'%s\'"%(vm_id)
			cur.execute(query)
			self.cnx.commit()
			query = "UPDATE vm_usage SET terminate = current_timestamp where vm_id=\'%s\'"%(vm_id)
			cur.execute(query)
			self.cnx.commit()
			cur.close()
			return 1
		except db.Error as err:
			print("something went wrong: %s"%err)
			return 0
	
	def del_em_info(self,em_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT * FROM emulators WHERE em_id = \'%s\' AND active = 1"%(em_id)
			#print query
			cur.execute(query)
			#print cur.fetchone()
			if cur.fetchone()is None:
				return 0
			query = "UPDATE emulators SET active = 0 WHERE em_id = \'%s\'"%(em_id)
			cur.execute(query)
			self.cnx.commit()
			query = "UPDATE em_usage SET terminate = current_timestamp where em_id=\'%s\'"%(em_id)
			cur.execute(query)
			self.cnx.commit()
			cur.close()
			return 1
		except db.Error as err:
			print("something went wrong: %s"%err)
			return 0
		
	def get_flavor(self,flavor_id):
		try:
			cur = self.cnx.cursor()
			query = "SELECT cpu,ram,storage FROM flavors WHERE flavor_id = \'%s\'"%(flavor_id)
			cur.execute(query)
			flv = cur.fetchone()
			cur.close()
			return flv
		except db.Error as err:
			print("something went wrong"%err)
			return None