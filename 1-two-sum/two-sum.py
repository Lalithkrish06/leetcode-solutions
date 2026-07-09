class Solution(object):
    def twoSum(self, nums, target):
     check = {}
     for i,num in enumerate(nums):
        difference = target-num
        if difference in check:
            return[check[difference],i]
        check[num] = i    
    