def solution():
    numb = 430043 
    k = 2
    l = 0
    r = k - 1
    result = 0
    numStr = str(numb)
    while(r < len(numStr)):
        divisor = int(numStr[l:r+1])
        if(divisor != 0 and (numb % divisor == 0)):
            result += 1
        l +=1 
        r += 1
    print(result)
    pass

solution()