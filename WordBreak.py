class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dictSet = set(wordDict)
        i = 0
        j = 0
        n = len(s)
        while(i < n and j < n):
            if(s[i:j + 1] in dictSet):
                i = j + 1
                j = i
            else:
                j += 1
        if(i < n):
            return False 
        return True 
        """
        i = 0
        j = 0
        while(i < n and j < n):
            if(s[i:j + 1] in dictSet):
                i = i + 1
                j = i + 1
                continue
            else:
                j += 1
        if(i < n):
            return False 
        return True 
                    
        """
print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))