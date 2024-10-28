from collections import deque
def solution(no, prerequisites):
    adjList = {}
    for prereq in prerequisites:
        if prereq[0] in adjList:
            adjList[prereq[0]] = adjList[prereq[0]].append(prereq[1])
        else:
            adjList[prereq[0]] = [prereq[1]]
    print(adjList)
    visited = [False for _ in range(no)]
    indegree = [0 for _ in range(no)]
    for key in adjList.keys():
        for neigh in adjList[key]:
            indegree[neigh] += 1
    print(indegree)
    q = deque()
    for i in range(len(indegree)):
        if(indegree[i] == 0):
            q.append(i)
            break
    ts = []
    if(len(q) != 0):
        while(len(q) != 0):
            node = q.popleft()
            visited[node] = True
            ts.append(node)
            if node in adjList:
                for neigh in adjList[node]:
                    if(visited[neigh] == False):
                        indegree[neigh] = indegree[neigh] - 1
            for i in range(len(indegree)):
                if indegree[i] == 0 and visited[i] == False:
                    q.append(i)
            pass
        if len(ts) == no:
            return ts
        else:
            return -1
    else:
        return -1

print(solution(3, [[1,0], [2,1]]))