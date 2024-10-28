class Solution:
    def numDecodings(self, s: str) -> int:
        validChars = set()
        for i in range(1,27):
            validChars.add(str(i))
        
        n = len(s)
        
        def rec(idx):
            if(idx >= n):
                return 1
            else:
                pickOne = 0
                pickTwo = 0
                if(s[idx] in validChars):
                    pickOne += rec(idx+1)
                if((i != n-1) and (s[idx:idx+2] in validChars)):
                    pickTwo += rec(idx+2)
                return pickOne+pickTwo
        
        return rec(0)

print(Solution().numDecodings("226"))