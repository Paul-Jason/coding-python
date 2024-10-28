n = 3
points = [[1,2,5], [3,1,1], [3,3,3]]
def rec(day, activity, ans):
    ans += points[day][activity]
    if(day < n - 1):
        day += 1
        if(activity == 0):
            rec(day, 1, ans)
            rec(day, 2, ans)
        if(activity == 1):
            rec(day, 0, ans)
            rec(day, 2, ans)
        if(activity == 2):
            rec(day, 0, ans)
            rec(day, 1, ans)
    return ans

print(max(rec(0, 0, 0), rec(0,1,0), rec(0,2,0)))
