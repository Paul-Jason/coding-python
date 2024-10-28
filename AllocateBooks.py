def solution(arr, noOfStudents):
    totalSum = sum(arr)
    for i in range(1, totalSum + 1):
        
    if(len(arr) < noOfStudents):
        return -1

print(solution())