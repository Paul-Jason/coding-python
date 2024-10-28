from os import *
from sys import *
from collections import *
from math import *

def ayushGivesNinjatest(days, chapters, times):
    # Write your code here.
    low = max(times)
    high = sum(times)
    result = 0
    for i in range(low, high+1):
        noOfDays = getNoOfDays(times, i)
        if(noOfDays == days):
            result = noOfDays
            break
    if(result == 0):
        result = low
    return result

def getNoOfDays(times, timeAllowed):
    noOfDays = 0
    i = 0
    j = 0
    n = len(times)
    while(i<n):
        sumTillHere = 0
        while(j<n):
            sumTillHere += times[j]
            if(sumTillHere > timeAllowed):
                break
            j += 1
        i = j
        noOfDays += 1
    return noOfDays

print(ayushGivesNinjatest(8, 9, [7,10,5,2,8,4,5,10])

"""
10
7 
10 
5 2 
8 
4 5 
10 
"""