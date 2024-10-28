"""
N
moves - R, F, Learn new
"""
n = 3
#points = [[1,2,5], [3,1,1], [3,3,3]]
#points = [[10,40,70], [20,50,80], [30,60,90]]
points = [[18,11,19], [4,13,7], [1,8,13]]
# points = [[10, 50, 1], [5, 100, 11]]
dp = [[0 for _ in range(3)] for _ in range(n)]
print(dp)
maxMerit = 0
for i in range(3):
    dp[0][i] = points[0][i]
    maxMerit = max(maxMerit, dp[0][i])
for day in range(1,n):
    for activity in range(3):
        if(activity == 0):
            dp[day][0] = points[day][activity] + max(dp[day-1][1], dp[day-1][2]) 
        if(activity == 1):
            dp[day][1] = points[day][activity] + max(dp[day-1][0], dp[day-1][2]) 
        if(activity == 2):
            dp[day][2] = points[day][activity] + max(dp[day-1][0], dp[day-1][1]) 
        maxMerit = max(maxMerit, dp[day][activity])
print(maxMerit)
