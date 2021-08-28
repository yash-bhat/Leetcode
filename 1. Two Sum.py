"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        
        for i in range(len(nums)):
            dict[nums[i]] = i
            
        for i in range(len(nums)):
            comple = target-nums[i]
            if (comple in dict.keys()):
                if (i != dict[comple]):
                    return [i,dict[comple]]
                
                
       #ANOTHER SOLUTION
    
       for i in range(len(nums)):
            fix_ele = nums[i]
            if target-fix_ele in nums[i+1:]:
                return [i,i+nums[i+1:].index(target-fix_ele)+1]
