"""
class Node:

start going through the strings 
check if the node is in graph if yes check reorder according to prev node
keep doing for all 
"""
from collections import deque
def sol(strings):
    adjList = {}
    for string in strings:
        for i in range(len(string)):
            present = string[i]
            if(i == 0):
                if(present not in adjList):
                    adjList[present] = set()
            else:
                prev = string[i-1]
                if(present not in adjList):
                    adjList[present] = set()
                if(prev != present):
                    adjList[prev].add(present)
    print(adjList)
    indegree = {}
    for key in adjList:
        indegree[key] = 0
    for key in adjList:
        for neigh in adjList[key]:
            indegree[neigh] += 1
    print(indegree)
    q = deque()
    for key in indegree:
        if(indegree[key] == 0):
            q.append(key)
    order = []
    while(q):
        ch = q.popleft()
        order.append(ch)
        for neigh in adjList[ch]:
            indegree[neigh] -= 1
            if(indegree[neigh] == 0):
                q.append(neigh)
    if(len(order) == len(adjList)):
        print(order)
    else:
        print(-1)
    
    
"""
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
  
  top sorting 
  w r t f e  
  0 2 4 2 0
  
  w -> r -> t
"""

sol(["z","x","z"])               