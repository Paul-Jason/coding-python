from typing import List
from collections import deque


def minimumTimeTakingPath(heights):
    dp = [float("inf") for _ in range(len(heights))]
    return mem(0, heights, len(heights), dp)

def mem(i, heights, n, dp):
    if(i == n - 1):
        return 0
    if(dp[i] != -1):
        return dp[i]
    else:
        minSteps = float("inf")
        for j in range(i+1,i+heights[i]+1):
            if(j <= n-1):
                minSteps = min(minSteps, 1 + rec(j, heights, n))
        dp[i] = minSteps
        return dp[n-1]
    
def minimumTimeTakingPathRec(heights):
    return rec(0, heights, len(heights))

def rec(i, heights, n):
    if(i == n - 1):
        return 0
    else:
        minSteps = float("inf")
        for j in range(i+1,i+heights[i]+1):
            if(j <= n-1):
                minSteps = min(minSteps, 1 + rec(j, heights, n))
        return minSteps

print(minimumTimeTakingPath([2,3,1,1,4]))