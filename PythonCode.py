#The following program will create an Undirected & Unweighted Graph.
Final = {}
class Graph():
    def __init__(self, node):
        self.node = node
        self.graph = []

    def AddValue(self, a,):
       self.graph.append(a)
       dic = {}
       dic[self.node]=self.graph
       
       Final[self.node]=self.graph


v = Graph(3)
v.AddValue(4)
v1 = Graph(4)
v1.AddValue(3)
v1.AddValue(5)
v2 = Graph(5)
v2.AddValue(6)

print(Final)



