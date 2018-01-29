class Solution:

    def bfs(self, adj, start, n):
        distance = [-1]*n
        q = []

        q.append(start)
        distance[start] = 0

        while len(q)>0:
            node = q.pop()

            for nbr in adj[node]:
                if distance[nbr]==-1:
                    distance[nbr] = distance[node]+1
                    q.append(nbr)

        max_dist = 0
        node_id = -1

        for i in range(len(distance)):
            if distance[i] > max_dist:
                max_dist = distance[i]
                node_id = i
        return (node_id, max_dist)


    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        adj = [[]]*len(A)
        root = -1
        #build adjacency list
        for i in range(len(A)):
            if A[i] == -1:
                root = i
                continue
            if len(adj[i])==0:
                adj[i] = []
            if len(adj[A[i]])==0:
                adj[A[i]] = []
            adj[i].append(A[i])
            adj[A[i]].append(i)

        #start visiting from root node with bfs
        node, max_distance = self.bfs(adj, root, len(A))

        #start visiting from the end node found in step 2 to find the other end
        node, max_distance = self.bfs(adj, node, len(A))

        return max_distance
