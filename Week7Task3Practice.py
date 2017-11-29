import unittest
#The following program will create an Unweighted Undirected Graph and perfomr a DFS on it.
Final = {}

class Graph():
    #This function will create the edges in a set for what nodes connect to each other.
    def __init__(self, node):
        self.node = node
        self.edges = set([])
    #This function will be used to add the edges the user enters to the dictionary Final.
    def AddValue(self, Link,):
       self.edges.add(Link)
       dic = {}
       dic[self.node]=self.edges
       
       Final[self.node]=self.edges
    #This final function is used to perfrom the DFS and output the results to the user.
    def dfs(Begining):
        VisitedNode, stack = set(), [Begining]
        while stack:
            vertex = stack.pop()
            if vertex not in VisitedNode:
                VisitedNode.add(vertex)
                stack.extend(Final[vertex] - VisitedNode)
        print(VisitedNode)
        return VisitedNode

        #The following code will save the Output to a text file
        output = str(VisitedNode)
        file = open('DFS.txt', 'w')
        file.write(output)
        file.close()
    
	   
v = Graph(3)
v1 = Graph(4)
v2 = Graph(5)
v3 = Graph(6)
v.AddValue(4)
v1.AddValue(3)
v1.AddValue(5)
v2.AddValue(4)
v2.AddValue(6)
v3.AddValue(5)

print(Final)

Graph.dfs(5)
#The code below will unit test my porgram 
class Tests (unittest.TestCase):
    def test_DFS(self):
                   
        v = Graph(3)
        v1 = Graph(4)
        v2 = Graph(5)
        v3 = Graph(6)
        v.AddValue(4)
        v1.AddValue(3)
        v1.AddValue(5)
        v2.AddValue(4)
        v2.AddValue(6)
        v3.AddValue(5)
        Graph.dfs(3)
        self.assertEqual(Graph.dfs(3), {3, 4, 5, 6})

    def test_DFS1(self):
                   
        v = Graph(3)
        v1 = Graph(4)
        v2 = Graph(5)
        v3 = Graph(6)
        v.AddValue(4)
        v1.AddValue(3)
        v1.AddValue(5)
        v2.AddValue(4)
        v2.AddValue(6)
        v3.AddValue(5)
        Graph.dfs(3)
        self.assertEqual(Graph.dfs(4), {4, 3, 5, 6})
if __name__=='__main__':
      unittest.main()
