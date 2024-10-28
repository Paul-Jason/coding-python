def wordSearch(mat, n, m, queries, q):
    # Write your code here.
    res = []
    for no in range(q):
        queryWord = queries[no]
        visited = [[False for _ in range(m)] for _ in range(n)]
        isWordPossible = True
        for char in queryWord:
            isCharThere = False
            for i in range(n):
                for j in range(m):
                    if(visited[i][j] != True):
                        if(mat[i][j] == char):
                            isCharThere = True
                            visited[i][j] = True 
                            break
                if(isCharThere):
                    break
            if(isCharThere == False):
                isWordPossible = False
                break
        if(isWordPossible):
            res.append(1)
        else:
            res.append(0)
    return res

print(wordSearch([["L"], ["O"], ["L"], ["Z"],["Z"]], 5, 1, ["LLZZ"], 1));