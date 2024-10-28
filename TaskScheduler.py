import heapq
class Solution:
    def run(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        taskMap = {}
        for task in tasks:
            if task in taskMap:
                taskMap[task] = taskMap[task]+1
            else:
                taskMap[task] = 1
        print(taskMap)
        heap = []
        for taskName, repeatNo in taskMap.items():
            heapq.heappush(heap, -1 * repeatNo )
        print(heap)
        maxLen = -1 * heap.pop()
        result = (n + 1) * (maxLen - 1) + 1
        while(len(heap) != 0):
            heapItem = -1 * heap.pop()
            if(heapItem == maxLen):
                result += 1
            else :
                break
        print(result)

Solution().run()

"""
a-3
b-3 
max - a 
n - 3 
a - - - a - - - a
"""