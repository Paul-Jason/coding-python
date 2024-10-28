def longestCommonMem(str1, str2, m, n, dp):
    if(m == 0 or n == 0):
        return 0
    if(dp[m-1][n-1] != -1):
        return dp[m-1][n-1]
    else:
        if(str1[m-1] == str2[n-1]):
            dp[m-1][n-1] =  1 + longestCommonMem(str1, str2, m-1, n-1, dp)
        else:
            dp[m-1][n-1] = max(longestCommonMem(str1, str2, m-1, n, dp), longestCommonMem(str1, str2, m, n-1, dp))
    return dp[m-1][n-1]

dp = [[-1 for _ in range(4)] for _ in range(3)]
print(longestCommonMem("abc", "cadb", 3, 4, dp))
