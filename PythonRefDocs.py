print("first print")
# indentation
if 5 > 2 :
    print("indentation")

# variables
x = 2
y = "paul"
z = str(3)

print(x,y,z)

# function
def myFun():
    print("my function")

myFun()

# data types - str, int, float, list, tuple, dict, set, bool, None, there is nothing like character

xStr = "a"
xStr2 = 'a'
xInt = 9
xFloat = 9.0
xList = ["apple", "mango"]
xTuple = ("apple", "mango")
xDict = {"name": "Paul", "age": 36}
xSet = {"Paul", "Paul"}
xBool = True
xNone = None

#list 
xList.append("test")
xList.sort()
xList.sort(key=lambda x : x, reverse= True)
del xList[0]
print(xList)

#set 
# is the only departure where we use add and remove
xSet.add("test")
if "test" in xSet:
    xSet.remove("test") # else KeyError
print(xSet)

#dict 
xDict["key2"] = "value2"
del xDict["key2"]
keyList = xDict.keys()
valueList = xDict.values()
keyValueTuple = xDict.items()
print(xDict["key2"])

import random
print('range', random.randrange(1,6))

# strings - are arrays
str1 = """abc
cdf"""

print(str1)
print(str1[0])

for char in str1:
    print(char)

print(len(str1))

if "abc" in str1:
    print("Yes")

if "cde" not in str1:
    print("Yes")

print(str1[1:3])
print(str1[:3])
print(str1[5:])
print("from last", str1[-5:-2])
print("upper", str1.upper())
print("lower", str1.lower())
print("abc".replace("ab", "d"))

str2 = "hello world"

print(str2.split(" "))

#  we cannot concate string and number directly 
print("test " + str(1))
print("I am Paul {}".format(36))

str3 = "hello world"

print(str2 == str3)

# operators

print(x > 5 and y < 5)

x = [1,2]
y = [1,2]

print("true", x == y)
print("false", x is y) # obj by reference, this is imp

# list 
list1 = [1,2,4]
list2 = [1, "two"] # can be any type

list1.insert(2, 3) # insert at particular index 
print(list1)

list1.extend(list2)
print(list1)

list1.remove("two")
print(list1)

list1.pop(1)
print(list1)

list1.pop() #remove last item
print(list1)

del list1[1]
print(list1)

list1.append(3)
list1.sort(reverse=True)
print(list1)

list2 = [[1,2],[3,4]]
list2.sort(key=lambda ele: ele[1], reverse= True)
print(list2)

for i in range(len(list2)):
    print(list2[i])

# dict 

dict = {"key1": 1, "key2": 2}

print(dict["key1"])

print(dict.keys())
print(dict.get("key1"))
dict["key1"] = 3
print(dict["key1"])

if "key" in dict:
    print("key")

# OOPS

class Person:
    def __init__(self, name, age, __private_age):
        self.name = name
        self.age = age
        self.__private_age = __private_age #this is private variable not accessible outside

    def __str__(self) -> str:
        return f"toString"
    
    def myFunc(self):
        print("my fun", self.name)

    def getPrivate(self):
        return self.__private_age

p1 = Person('Paul', 26, 28)
print('age', p1.age)
print('to string', p1)
p1.myFunc()
print(p1.getPrivate())

#exception 

try:
    print('sometry')
except TypeError:
    raise TypeError("test")
except:
    print('general exception')
    raise Exception("test")
else:
    pass
finally:
    pass

# input 

# p = input()
# print(type(p))

# heap 
import heapq
heap = [1,2,3]

heapq.heapify(heap) #o(n)
heapq.heappush(heap, 4) #o(logn)
print(heapq.heappop(heap)) #o(logn)

# deque 
from collections import deque
stack = deque()
stack.appendleft("a")
stack.popleft()

# hash function 
str10 = "string"
hashedStr = hash(str10)
print(str10)
print(hashedStr)
print(hash(str10))
# but this can product duplicates 

#random 
import random

print(random.random())
print(random.randrange(1,5))
print(random.choice(["1","2","3","a","b","c"]))

from collections import Counter
str11 = "absbass"
str12 = "abcabcc"
print(Counter(str11) - Counter(str12))

list1 = [0] * 26
print(list1)

list10 = [0 for _ in range(26)]
print(list10)

val = ord("b") #ascii value
print(val)

# divison 
num = 9 // 4 # output - 2 
num1 = 9 % 4 # output - 1 
num2 = 9 / 4 # output - 2.25

# math 
import math
print(math.log(9,2))

#permutations & combinations 
import itertools

string = "aba"
permutations = list(itertools.permutations(string, len(string))) # order matters
# permutations = set(itertools.permutations(string, len(string))) # when you want unique permutations 
combinations = list(itertools.combinations(string, len(string))) # order doesn't matter
print(permutations)
print(combinations)

listlist = [[1,3],[3,2],[2,4]]
listlist.sort(key= lambda x:x[1])
print(listlist)

# bit wise operations
num10 = 10
num11 = 11 
numor = num10 | num11 
numand = num10 & num11 
numxor = num10 ^ num11 

x = float("inf")
print(x > 100000)
y = float("-inf")

# tree
class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        pass

print("5".split(" "))

print([int(i) for i in input().split(" ")])

"""
you can not directly modify the parent function variables inside child function variables 
you need to use nonlocal s
"""

charToAscii = ord('a')
print(charToAscii)

asciiToChar = chr(97)
print(asciiToChar)
