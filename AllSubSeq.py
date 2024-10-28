
def allSubSequences(prefix, idx, string, res):
    if(idx == len(string)):
        return
    else:
        for i in range(idx, len(string)):
            temp = prefix + string[i]
            res.append(temp)
            allSubSequences(temp, i + 1, string, res)
    return res

print(allSubSequences("", 0, "312", []))