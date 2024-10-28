"""
array 
target 

sum >= target

[2,3,1,2,4,3]

target = 7 

brute force 
----
try every sub array 

for i 
    for j 
        calculate sum 

time - O(n^3)

dp 
--
create a 2d array and create sum ?

time - O(n ^ 2)
space - O(n ^ 2)
"""

#dp 
def solution(arr, target):
    sumStore = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        sumStore[i][i] = arr[i]
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sumStore[i][j] = sumStore[i][j-1] + arr[j]
            if(sumStore[i][j] >= target):
                if(result == 0):
                    result = j - i + 1
                else:
                    result = min(result, j - i + 1)
    print(result)
    pass

solution([1,4,4],4)

"""
sliding window 

[2,3,1,2,4,3]
         l 
           r 
target = 7

l = 0, r = 0, sum = arr[0], min = float("inf")

while r < n - 1;
    if(sum >= target):
        min = min(min, r - l + 1)
        sum -= arr[l]
        l--;
    else:
        r++;
        sum += arr[r]
"""

