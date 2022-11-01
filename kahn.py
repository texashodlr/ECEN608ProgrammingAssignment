#This is going to be a Kahn's Algorithm implemented in python for ECEN608 Fall22 programming assignment
from collections import defaultdict

#This class represents the graph
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) # dict containing the adjaceny list.
		self.V = vertices # No. of vertices
		
	#function to add an edge to a graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		
	# The function to do topo sort.
	def topologicalSort(self):
	
		# Create a vector to store indegrees of all
		# Vertices init all indegrees as 0.
		in_degree = [0]*(self.V)
		
		#Traverse adj lists to fill indegrees of # of vertices this step takes O(E+V) time
		for i in self.graph:
			for j in self.graph[i]:
				in_degree[j] += 1
		
		#Create an queue and enqueue all vertices with indegree 0
		queue = []
		for i in range(self.V):
			if in_degree[i] == 0:
				queue.append(i)
		
		# Init count of visited vertices
		cnt = 0
		
		#Create a vector to store the result (topo ordering of the vertices)
		top_order = []
		
		#1by1 dequeue vertices from queue and enqueue adjacents if indegree of adj becomes 0
		while queue:
		
			#extract  front of queue (or perform dequeue) and add it to the topo ordering
			u = queue.pop(0)
			top_order.append(u)
			
			#Iterate through all neighbor nodes of dequeued node u and decrease their in-degree by 1
			for i in self.graph[u]:
				in_degree[i] -= 1
				#if indegree becomes 0 then add it to the queue
				if in_degree[i] == 0:
					queue.append(i)
			cnt += 1
		
		#check if there was a cycle
		if cnt != self.V:
			print ("There exists a cycle in this graph")
		else : 
			#print topo ordering
			print (top_order)
		
g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()