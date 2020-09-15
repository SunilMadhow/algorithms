class Edge:
	def __init__(self, capacity, whither, thither, residual=0, load = 0):
		self.capacity = capacity
		self.residual = residual
		self.load = load
		self.whither = whither
		self.thither = thither
	def __str__(self):
		return "%d / %d" % (self.load, self.capacity)
	def __repr__(self):
		return self.__str__()
	def add_flow(self, amt):
		self.load = self.load + amt
		self.residual = self.residual - amt

	def get_available_capacity(self):
		return self.capacity - self.load

	def is_saturated(self):
		return self.get_available_capacity() == 0

from queue import Queue
class FlowNetwork:
	def __init__(self, sources, sinks, graph):
		self.sources = sources
		self.sinks = sinks
		self.graph = self.build_network(graph)
		self.sinks = [i + 1 for i in sinks]
		self.max_edge_capacity = 10**6

	def build_network(self, arr):
		total_source_flow = 0
		for i in self.sources:
			for j in arr[i]:
				total_source_flow = total_source_flow + j
		total_sink_flow = 0
		for i in range(0, len(arr)):
			for j in range(0, len(arr)):
				if j in self.sinks:
					total_sink_flow = total_sink_flow + arr[i][j]
		graph = [[None] * (len(arr) + 2) for _ in range(0, len(arr) + 2)]

		for i in self.sources:
			graph[0][i + 1] = Edge(total_source_flow, 0, i +1)
		for j in self.sinks:
			graph[j + 1][-1] = Edge(total_sink_flow, j + 1, len(arr) + 2)

		for i in range(len(arr)):
			for j in range(len(arr)):
				if arr[i][j] != 0: 
					graph[i + 1][j + 1] = Edge(arr[i][j], i + 1, j + 1)
				else:
					graph[i + 1][j + 1] = None
		return graph

	def augment_path(self, path): #path is a list of edges
		bottleneck = self.max_edge_capacity
		for i in range(0, len(path) - 1):
			if self.graph[path[i]][path[i + 1]].get_available_capacity() < bottleneck:
				bottleneck = self.graph[path[i]][path[i + 1]].get_available_capacity()
		for i in range(0, len(path) - 1):
			self.graph[path[i]][path[i + 1]].add_flow(bottleneck)

	def BFS(self):
		visited = [False]*len(self.graph)
		queue = Queue()
		queue.put([0])
		# print(self.graph)
		while not queue.empty():
			path = queue.get()
			vertex = path[-1]
			# print(vertex)
			if vertex == len(self.graph) - 1:
				return path
			elif visited[vertex] == False:
				for i in range(0, len(self.graph[vertex])):
					if self.graph[vertex][i] != None and not self.graph[vertex][i].is_saturated():
						new_path = list(path)
						new_path.append(i)
						queue.put(new_path)
					visited[vertex] = True

	def get_sink_flow(self):
		flow = 0
		for i in self.sinks:
			flow = flow + self.graph[i][-1].load
		return flow

	def edmunds_karp(self):
		while True:
			path = self.BFS()
			if path is None:
				return self.get_sink_flow()
			self.augment_path(path)
			
def solution(entrances, exits, path):
    # Your code here
    f = FlowNetwork(entrances, exits, path)
    return f.edmunds_karp()
    # return 6


print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))