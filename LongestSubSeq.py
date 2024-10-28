def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    arr.sort()
    print(arr)
    left = 0
    right = 0
    longest = 1
    # 20 30 33 34 35 
    while(left <= len(arr) - 1):
        tempLongest = 1
        while((right < len(arr) - 1) and ((arr[right + 1] == arr[right] + 1) or (arr[right] == arr[right + 1]))):
            if(arr[right + 1] == arr[right] + 1):
                tempLongest += 1
            right += 1
        longest = max(longest, tempLongest)
        if(right > left):
            left = right + 1
        else:
            left += 1
        right = left
    return longest

print(lengthOfLongestConsecutiveSequence([4,17,1,7,13,12,10,16,25,21,12,22,23,11,14,15,7,2,15,6], 20))