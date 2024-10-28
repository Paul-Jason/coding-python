import heapq
def mergeIntervals(intervals):
    # Write your code here.
    result = []
    intervals.sort(key = lambda interval : interval[0])
    i = 0
    while(i < len(intervals) - 1):
        j = i + 1
        while(j < len(intervals) and intervals[j - 1][1] >= intervals[j][0]):
            j += 1
        result.append([intervals[i][0], intervals[j - 1][1]])
        i = j
    if(i == len(intervals) - 1):
        result.append([intervals[i][0], intervals[i][1]])
    return result
    
print(mergeIntervals([[1,4],[3,5],[8,9],[6,8],[10,12]]))

"""
[[1,4],[3,5],[8,9],[6,8],[10,12]]
[[1, 4], [3, 5], [6, 8], [8, 9], [10, 12]
                                    i
pseudo code is the final code
"""

set1 = set()
set1.add((1,2))
set1.add((1,2),(2,3))
print(set1)