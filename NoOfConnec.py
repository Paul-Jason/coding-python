"""
visited 
for every node 
    not visited 
        bfs 
        no += 1

should we consider cycles 

"""
from collections import deque

def noOfConnect(n, edges):
    
    def bfs(start):
        q = deque()
        q.append(start)
        while q:
            node = q.popleft()
            visited.add(node)
            if node in adjList:
                for neigh in adjList[node]:
                    if neigh not in visited:
                        q.append(neigh)
    
    adjList = {}
    for edge in edges:
        if edge[0] in adjList:
            adjList[edge[0]].append(edge[1])
        else:
            adjList[edge[0]] = [edge[1]]
        if edge[1] in adjList:
            adjList[edge[1]].append(edge[0])
        else:
            adjList[edge[1]] = [edge[0]]
    visited = set()
    no = 0
    for i in range(n):
        if i not in visited:
            bfs(i)
            no += 1
    return no
    
print(noOfConnect(7, [[0, 1], [2, 3], [4, 5]]))