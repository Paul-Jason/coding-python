from collections import deque
def topologicalSort(adj, V, E):
    indegree = [0 for _ in range(V)]
    for key in adj.keys():
        for node in adj[key]:
            indegree[node] += 1
    visited = [False for _ in range(V)]
    q = deque()
    for node in range(len(indegree)):
        if(indegree[node] == 0):
            q.append(node)
            
    res = []
    while(len(q) != 0):
        node = q.popleft()
        visited[node] = True
        res.append(node)
        if node in adj:
            for neigh in adj[node]:
                if(indegree[neigh] == 0 and visited[neigh] == False):
                    q.append(neigh)
                else:
                    indegree[neigh] -= 1
    
    for node in range(len(indegree)):
        if(indegree[node] == 0 and visited[node] == False):
            visited[node] = True
            res.append(node)
    if(len(res) == V):
        return res 
    return []

print(topologicalSort({0:[1], 2:[1]},3,2))