def getLCS(str1, str2):
    # Write your code here.

    def getSubSeq(idx, prefix, st, n, allSubSeq):
        if idx > n - 1:
            allSubSeq.append(prefix)
        else:
            temp = prefix + st[idx]
            getSubSeq(idx + 1, temp, st, n, allSubSeq)
            getSubSeq(idx + 1, prefix, st, n, allSubSeq)
        return allSubSeq

    subSeq1 = []
    subSeq2 = []

    subSeq1 = getSubSeq(0, "", str1, len(str1), subSeq1)
    subSeq2 = getSubSeq(0, "", str2, len(str2), subSeq2)
    
    longSubSeq = ""

    for seq1 in subSeq1:
        for seq2 in subSeq2:
            if(seq1 == seq2 and len(seq1) > len(longSubSeq)):
                longSubSeq = seq1
    return longSubSeq

print(getLCS("pqr", "tpuqvr"))