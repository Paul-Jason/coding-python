from os import *
from sys import *
from collections import *
from math import *

def longestRepeatingSubsequence(st, n):

    allSubSeq = set()
    longSubSeq = ""

    def getLongest(idx, prefix):
        nonlocal allSubSeq
        nonlocal longSubSeq
        if(idx > n - 1):
            if prefix in allSubSeq:
                if(len(prefix) > len(longSubSeq)):
                    longSubSeq = prefix
            else:
                allSubSeq.add(prefix)
        else:
            temp = prefix + st[idx]
            getLongest(idx + 1, temp)
            getLongest(idx + 1, prefix)
    
    getLongest(0, "")
    return longSubSeq

print(longestRepeatingSubsequence("ABCBDCD", 7))