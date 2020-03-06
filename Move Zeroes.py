"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        res1 = list(filter(lambda a: a != 0, nums))

        res2 = [0]*(l-len(res1))

        res = res1+res2

        for i in range(l):
            nums[i]=res[i]
    
        
