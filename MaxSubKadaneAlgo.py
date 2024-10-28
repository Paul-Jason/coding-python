def maxSubArraySum(arr):
    currentSum = 0
    maxSum = float("-inf")
    for num in arr:
        currentSum += num
        maxSum = max(maxSum, currentSum)
        if(currentSum < 0):
            currentSum = 0
    return maxSum

print(maxSubArraySum([-2,-3,4,-1,-2,1,5,-3]))