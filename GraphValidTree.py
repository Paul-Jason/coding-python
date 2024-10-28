"""
find cycle in undirected grpah 
"""
from collections import deque
def isCyclic(edges):
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
    visited = set() # node and value as parent node
    q = deque()
    q.append((0,-1))
    isCyclic = False
    while(q):
        node = q.popleft()
        if node[0] in visited:
            isCyclic = True
            break
        else:
            visited.add(node[0])
        for neigh in adjList[node[0]]:
            if neigh == node[1]:
                continue
            q.append((neigh, node[0]))
    return isCyclic

print(isCyclic([[0,1], [0,2], [0,3], [1,4]]))
        
        