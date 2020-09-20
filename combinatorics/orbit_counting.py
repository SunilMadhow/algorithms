class Group: #not actually a group because it doesn't keep track of the set
	def __init__(self, w, h, s):
		self.w = w
		self.h = h
		self.num_vertices = w*h
		self.states = s
		self.group = self.generate_group_basis()
		while True:
			f = self.close_group()
			if not f:
				self.close_group()
			else:
				break
		self.cycles = self.build_cycle_table()
		

	def generate_group_basis(self): #generate switching of row i with all other rows and row j with all other rows
		G = []
		G.append(list(range(0, self.num_vertices)))
		for i in range(1, self.h):
			g = list(range(0, self.w * self.h))
			g[:self.w] = list(range(i * self.w, (i + 1) * self.w))
			g[i * self.w : (i + 1) * self.w] = list(range(0, self.w))
			G.append(g)
		for col in range(1, self.w):
			g = list(range(0, self.w * self.h))
			for row in range(0, self.h):
				g[row * self.w + col] = row *self.w
				g[row * self.w] = col +  self.w * row
			G.append(g)
		return G


	def close_group(self): #find a finite subgroup of self.group
		for i in range(0, len(self.group)):
			for j in range(0, len(self.group)):
				g_prime = [self.group[i][self.group[j][k]] for k in range(0, self.num_vertices)]
				if g_prime not in self.group:
					self.group.append(g_prime)
					return False
		return True


# 		print(self.group)

	def find_vertex_cycle(self, g): #find vertex cycles in element g of self.group
		cycles = [[0]]
		l = list(range(1, self.num_vertices))
		i = 0
		j = 0
		while len(l) > 0:
			z = cycles[i][j]
			if g[z] == z or g[z] == cycles[i][0]:
				cycles.append([l[0]])
				l.pop(0)
				i = i + 1
				j = 0
			else:
				cycles[i].append(g[z])
				j = j + 1
				l.remove(g[z])
		# print(cycles)
		return cycles

	def build_cycle_table(self):
		cycle_table = []
		for g in self.group:
			cycle_table.append(len(self.find_vertex_cycle(g)))
		return cycle_table
				
	def burnside(self):
		tally = 0
		for i in range(0, len(self.group)):
			tally = tally + (self.states)**self.cycles[i]
		return tally/len(self.group)


def solution(w, h, s):
	s = Group(w, h, s)
	return str(long(s.burnside()))

# s = Group(2, 2, 3)
# print(len(s.group))
print(solution(11, 10, 3))