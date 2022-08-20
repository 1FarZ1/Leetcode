## my algoritheme 

class Solution(object):
    def search(self, nums, target):
        for i in nums:
            if i==target:
                return nums.index(target)
        return -1
    
    
print(removeDuplicates([1,1,2]))   


### binary search algoritheme
class Solution(object):
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while(low <= high):
            mid = (low + (high - low)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    
    ## another solution
class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -    