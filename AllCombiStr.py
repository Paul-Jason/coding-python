def allCombinations(idx, string, res):
    if(idx == len(string)):
        return
    else:
        for i in range(idx, len(string)):
            temp = swap(string, idx, i)
            res.add(temp)
            allCombinations(idx + 1, temp, res)
    return res

def swap(string, idx, i):
    if(idx == i):
        return string
    charIdx = string[idx]
    charI = string[i]
    return string[:idx] + charI + string[idx+1:i] + charIdx + string[i+1:]

print(allCombinations(0, "abcd", set()))