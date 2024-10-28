def nonOverlap(intervals):
    arr = [[i,j] for i,j in intervals]
    arr.sort(key = lambda x : x[1])
    n = len(arr)
    removedIdx = set()
    i = 0 
    while(i < n):
        j = i+1 
        if i not in removedIdx and j not in removedIdx:
            while(j<n and arr[i][1] > arr[j][0]):
                j += 1
                removedIdx.add(j)
        i = j
    return len(removedIdx) 

print(nonOverlap([[1,100],[11,22],[1,11],[2,12]]))