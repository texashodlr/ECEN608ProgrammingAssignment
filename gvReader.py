from graphviz import Source
#Source.from_file('graph.gv')
graph = open('graph.gv','r')
#print("Reading begin")
count = 0
for line in graph:
        if(("->") in line):
            #print(line.replace(" ",""))
            u1 = int(line[1])
            u2 = int(line[6])
            if(u2 > count):
                count = u2
            print(u1)
            print(u2)
print(count)
graph.close()

# Dummy graph saved in case
#g= Graph(9)
#g.addEdge(0, 1);
#g.addEdge(0, 2);
#g.addEdge(0, 3);
#g.addEdge(0, 4);
#g.addEdge(2, 5);
#g.addEdge(1, 6);
#g.addEdge(1, 7);
#g.addEdge(5, 0);
#g.addEdge(4, 0);
#g.addEdge(4, 1);
#g.addEdge(2, 3);
#g.addEdge(3, 1);
