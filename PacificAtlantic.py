from collections import deque
class Solution:
    def pacificAtlantic(self, heights):
        """
        canFlowP 
        canFlowA 

        dfs 
        start at a cell 
        traverse in all four directions where ever possible 
        see if you can reach pacific and atlantic 

        1 2 2 
        3 2 3
        2 4 5

        """
        m = len(heights)
        n = len(heights[0])
        result = []
        canFlowPDp = [[None for _ in range(n)] for _ in range(m)]
        canFlowADp = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                canFlowP = False 
                canFlowA = False
                st = deque()
                st.append([i,j])
                visited = [[False for _ in range(n)] for _ in range(m)]
                while(len(st) != 0):
                    co = st.pop()
                    visited[co[0]][co[1]] = True
                    if(i == 0 or j == 0):
                        canFlowPDp[i][j] = True
                        canFlowP = True
                    if(i == m-1 or j == n-1):
                        canFlowADp[i][j] = True
                        canFlowA = True
                    if(canFlowP and canFlowA):
                        break
                    else:
                        if j != 0 and heights[i][j-1] <= heights[i][j] and not canFlowP and not visited[i][j-1]:
                            if(canFlowPDp[i][j-1] == True):
                                canFlowP = True
                            elif(canFlowPDp[i][j-1] == None):
                                st.append([i,j-1])
                        if j != n-1 and heights[i][j+1] <= heights[i][j] and not canFlowA and not visited[i][j+1]:
                            if(canFlowADp[i][j+1] == True):
                                canFlowADp = True
                            elif(canFlowADp[i][j+1] == None):
                                st.append([i,j+1])
                        if i != 0 and heights[i-1][j] <= heights[i][j] and not canFlowP and not visited[i-1][j]:
                            if(canFlowPDp[i-1][j] == True):
                                canFlowP = True
                            elif(canFlowPDp[i-1][j] == None):
                                st.append([i-1,j])
                        if i != m-1 and heights[i+1][j] <= heights[i][j] and not canFlowA and not visited[i+1][j]:
                            if(canFlowADp[i+1][j] == True):
                                canFlowADp = True
                            elif(canFlowADp[i+1][j] == None):
                                st.append([i+1,j])
                if(canFlowP and canFlowA):
                    result.append([i,j])
        return result 

        """
        time - O(n^4)
        space - O(n^2)
        """

print(Solution().pacificAtlantic([[1,2,2],[3,2,3],[2,4,5]]))