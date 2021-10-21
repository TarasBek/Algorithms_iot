from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, value):
		self.graph[u].append(value)

	def dfc_util(self, value, visited):
		visited.add(value)
		print(value)
		for neighbour in self.graph[value]:
			if neighbour not in visited:
				self.dfc_util(neighbour, visited)

	def dfc(self, value):
		visited = set()
		self.dfc_util(value, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfc(2)

