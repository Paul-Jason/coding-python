"""
nums, k

brute force 
---------
result = []
for i in range(len(nums)):
    left = i - k 
    right = i + k
    if(left >= 0 and right <= len(nums) - 1):
        result.append(getAvg(nums, left, right))
    else:
        result.append(-1)
return result 

getAvg(nums, left, right):
    sum = 0
    for i in range(left, right+1):
        sum += nums[i]
    return sum // (right - left + 1)

Time - O(n ^ 2)

optimal use dp 
--------------
result = []
sumDp = [0 for _ in range(len(nums))]
// k out of range of arr 
for i in range(0, 2 * k + 1):
    sumDp[k] = sumDp[k] + nums[i]
for i in range(k + 1, len(nums) - k):
    sumDp[i] = sumDp[i - 1] - nums[i - k - 1] + nums[i + k]
for i in range(len(nums)):
    left = i - k 
    right = i + k
    if(left >= 0 and right <= len(nums) - 1):
        result.append(getAvg(sumDp[i], left, right))
    else:
        result.append(-1)
return result 

getAvg(nums, left, right):
    return sum // (right - left + 1)

Time - O(n)
Space - O(n)

[7,4,3,9,1,8,5,2,6], k = 3

[0,0,0,37,32,34,0,0,0]


TIME TO SOLVE - 35 mins

"""

def solution(nums, k):
    result = [-1 for _ in range(len(nums))]
    sumDp = [0 for _ in range(len(nums))]
    sumDp[0] = nums[0]
    # k out of range of arr 
    if(len(nums) < 2 * k + 1):
        return result
    for i in range(0, 2 * k + 1):
        sumDp[k] = sumDp[k] + nums[i]
    for i in range(k + 1, len(nums) - k):
        sumDp[i] = sumDp[i - 1] - nums[i - k - 1] + nums[i + k]
    for i in range(len(nums)):
        left = i - k 
        right = i + k
        if(left >= 0 and right <= len(nums) - 1):
            result[i] = getAvg(sumDp[i], left, right)
    return result 

def getAvg(numsSum, left, right):
    return numsSum // (right - left + 1)

print(solution([7,4,3,9,1,8,5,2,6], 3))
print(solution([1000], 0))
print(solution([8], 1))
