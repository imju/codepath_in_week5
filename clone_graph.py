# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def printGraph(self, node):
        visited = {}

        q = []
        q.append(node)

        while len(q)>0:
            t = q.pop()
            statement =  't:'
            if visited.get(t.label):
                continue
            visited[t.label] = t
            statement += str(t.label) + '> neighbors:'
            for n in t.neighbors:
                statement += ' '+str(n.label)
                q.append(n)
            print statement

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited = {}
        created = {}
        #self.printGraph(node)
        q = []
        q.append((node, node.label))

        new_node = UndirectedGraphNode(node.label)
        created[node.label] = new_node

        while len(q)>0:
            node, label = q.pop()
            #print 'node.label:'+str(node.label) + ': neighbor count:'+str(len(node.neighbors))
            if visited.get(label):
                continue
            if created.get(label) is None:
                #print ' created: None:' + str(n.label)
                first = UndirectedGraphNode(n.label)
                created[label] = temp
            else:
                #print ' created: '+ str(n.label)
                first = created[label]

            visited[label] = node
            neighbors = []
            for n in node.neighbors:
                #print 'n.label:'+str(n.label)
                '''
                if created.get(n.label) is None:
                    #print ' created: None:' + str(n.label)
                    temp = UndirectedGraphNode(n.label)
                    created[n.label] = temp
                else:
                    #print ' created: '+ str(n.label)
                    temp = created[n.label]
                #visited[n.label] = temp
                for nbr in n.neighbors:
                    if created.get(nbr.label) is None:
                        new_nbr = UndirectedGraphNode(nbr.label)
                    else:
                        new_nbr = created[nbr.label]
                    if new_nbr not in temp.neighbors:
                        temp.neighbors.append(new_nbr)
                    q.append((nbr, nbr.label))
                if visited.get(n.label) :
                    continue
                '''

                if created.get(n.label) is None:
                    #print ' created: None:' + str(n.label)
                    temp = UndirectedGraphNode(n.label)
                    created[n.label] = temp
                else:
                    #print ' created: '+ str(n.label)
                    temp = created[n.label]
                #visited[n.label] = temp
                neighbors.append(temp)
                q.append((n, n.label))
            first.neighbors = neighbors
        #self.printGraph(new_node)

        #new_node = node
        return new_node

        # Definition for a undirected graph node
        # class UndirectedGraphNode:
        #     def __init__(self, x):
        #         self.label = x
        #         self.neighbors = []

        UndirectedGraphNode.__hash__ = lambda self: id(self)

        class Solution:
            def __init__(self):
                self.visited = {}

            # @param node, a undirected graph node
            # @return a undirected graph node
            def cloneGraph(self, node):
                if node not in self.visited:
                    new_node = UndirectedGraphNode(node.label)
                    self.visited[node] = new_node
                    new_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
                return self.visited[node]
