import unittest 
#The code below will create a
#Depth Fisrt Ssearh Program

#The graph variable is a dictionary storing the data
#regarding which nodes connect to each other.
graph = {1: set([2,3]),
         2: set([1,4,5]),
         3: set([2,6]),
         4: set([2]),
         5: set([2,6]),
         6: set([3,5])}

#Each node is added to the top of the stack when visited.
#If there is no extra nodes to be added i.e all nodes connected
#to the current node have been visited.
#Delete the top Node and continue to remove the Nodes from the stack
#Until 1 connects to a new Node or each Node has been traversed.
class DepthFirst ():
    def dfs(graph, Begining):
        VisitedNode, stack = set(), [Begining]
        while stack:
            vertex = stack.pop()
            if vertex not in VisitedNode:
                VisitedNode.add(vertex)
                stack.extend(graph[vertex] - VisitedNode)
        print(VisitedNode)
#The following code will save the Output to a text file
        output = str(VisitedNode)
        file = open('DFS.txt', 'w')
        file.write(output)
        file.close()
    
DepthFirst.dfs(graph, 1)
#The Output should be the following:
#{'E', 'D', 'F', 'A', 'C', 'B'}









