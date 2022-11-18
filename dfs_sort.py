#This is going to be a Depth-First-Search Algorithm implemented in python for ECEN608 Fall22 programming assignment
#Python program to print topological sorting of a DAG
from collections import defaultdict

#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Print contents of stack
        print (stack)

# Connector code to read the graphGen.py's files
g= Graph(16)
graph = open('graph.gv','r')
# Need to introduce two checks, if A is ## and if B is AA
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
# This code is contributed by Neelam Yadav