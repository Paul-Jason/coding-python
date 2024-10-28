from math import *
from collections import *
from sys import *
from os import *

def fourSum(arr, target):
    # Write your code here
    arr.sort()
    n = len(arr)
    result = False
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if i != j and j != k and k != i:
                        restEle = target - arr[i] - arr[j] - arr[k]
                        if(isFound(arr, restEle, i, j, k)):
                            result = True 
                            break
            if result == True:
                break
        if result == True:
                break
    if(result == True):
        print("Yes")
    elif(result == False):
        print("No")

def isFound(arr, restEle, i, j, k):
    low = 0
    high = len(arr) - 1
    isFound = False 
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == restEle and (i != mid and j != mid and k != mid)):
            isFound = True 
            break 
        # in case the mid already found and not satisfying the condition of indices you can switch left or right 
        elif(arr[mid] == restEle):
            l = mid - 1
            while(l >= low and arr[l] == restEle):
                if(i != l and j != l and k != l):
                    isFound = True 
                    break
                l -= 1
            l = mid + 1
            while(l <= high and arr[l] == restEle):
                if(i != l and j != l and k != l):
                    isFound = True 
                    break
                l += 1
        elif(arr[mid] < restEle):
            low = mid + 1
        else:
            high = mid - 1
        if(isFound):
            break
    return isFound

print(fourSum([1,3,3,10,2], 9))
print(fourSum([2,4,6,3,1,1], 20))

"""
for i 
    for j 
        for k
            for l

O(n ^ 4)
----

sorting 

i,j,k 
find l using binary search where l != i,j,k

O(n ^ 3 * log n)

----

arr.sort()
n = len(arr)
result = False
for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != j and j != k:
                    restEle = target - arr[i] - arr[j] - arr[k]
                    if(isFound(arr, restEle, i, j, k)):
                        result = True 
                        break
        if result == True:
            break
    if result == True:
            break

def isFound(arr, restEle, i, j, k):
    low = 0
    high = len(arr) - 1
    isFound = False 
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == restEle and (i != mid and j != mid and k != mid)):
            isFound = True 
            break 
        # in case the mid already found and not satisfying the condition of indices you can switch left or right 
        else if(arr[mid] == restEle):
            l = mid
            while(l >= low):
                l -= 1
                if(arr[l] == restEle and (i != l and j != l and k != l)):
                    isFound = True 
                    break
            l = mid
            while(l <= high):
                l += 1
                if(arr[l] == restEle and (i != l and j != l and k != l)):
                    isFound = True 
                    break
        else if(arr[mid] < restEle):
            low = mid + 1
        else:
            high = mid - 1

---

hmPairSum = {}
for i in range(n):
    for j in range(n);
        if i != j:
            sum = arr[i] + arr[j]


"""