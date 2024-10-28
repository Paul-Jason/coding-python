def search( nums, target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] == target):
                return mid
            # mid > target and mid > right which means left is sorted 
            elif(nums[mid] > target and nums[l] < nums[mid] and nums[l] <= target):
                r = mid - 1
            else:
                l = mid + 1
        return -1

print(search([1], 1))