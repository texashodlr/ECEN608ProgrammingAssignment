#This is going to be a Kahn's Algorithm implemented in python for ECEN608 Fall22 programming assignment
# A Python program to print topological sorting of a graph
# using indegrees
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do Topological Sort.
    def topologicalSort(self):

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of
        # vertices. This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
            print("There exists a cycle in the graph")
            #print(top_order)
        else:
            # Print topological order
            print(top_order)


g= Graph(16)
graph = open('graph.gv','r')
for line in graph:
        if(("->") in line):
            #Check 1
            # Case 1 X -> X
            if(line[2] == ' '):
                if(line[7] == '\n' or line[7] == ' '):
                    #print("Case 1: "+line[1]+", "+line[6])
                    g.addEdge(int(line[1]), int(line[6]))
                # Case 2 X -> XX
                elif (line[7] != '\n' or line[7] != ' '):
                    #print("Case 2: "+line[1]+", "+line[6:8])
                    g.addEdge(int(line[1]), int(line[6:8]))
            # Case 3 XX -> X
            elif(line[2] != '\n' and line[2] != ' '):
                if(line[7] == '\n' or line[7] == ' '):
                    #print("Case 3: "+line[1:3]+", "+line[6])
                    g.addEdge(int(line[1:3]), int(line[6]))
                # Case 4 XX -> XX
                elif(line[7] != '\n' and line[7] != ' '):
                    #print("Case 4: "+line[1:3]+", "+line[7:9])
                    g.addEdge(int(line[1:3]), int(line[7:9]))
graph.close()
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()