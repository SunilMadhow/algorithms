class StarMap:
	def __init__(self, w, h, s):
		self.w = w
		self.h = h
		self.num_vertices = w*h
		self.states = s
		self.group = self.generate_group_basis()
		

	def generate_group_basis(self): #generate switching of row i with all other rows and row j with all other rows
		G = []
		G.append(list(range(0, self.w*self.h)))
		for i in range(1, self.h):
			g = list(range(0, self.w * self.h))
			g[:self.w] = list(range(i * self.w, (i + 1) * self.w))
			g[i * self.w : (i + 1) * self.w] = list(range(0, self.w))
			# print(g)
			G.append(g)
		return G


	def close_group(self): #find a finite subgroup of self.group
		for i in range(0, len(self.group)):
			for j in range(0, len(self.group)):
				g_prime = [self.group[i][self.group[j][k]] for k in range(0, self.num_vertices)]
				if g_prime not in self.group:
					self.group.append(g_prime)

	def find_vertex_cycles(self): #iterate through all gEself.group and find cycles
		pass

s = StarMap(5, 3, 2)
s.close_group()
print(s.group)
