"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        
        
        for i,a in enumerate(nums):
            if i == 0:
                # print(a,i,nums[i+1:])
                if (a not in (nums[i+1:])):
                    return a
            elif i == len(nums)-1:
                # print(a,i,nums[:i])
                if a not in nums[:i]:
                    return a
            else:
                # print(a,i,nums[:i]+nums[i+1:])
                if a not in (nums[:i]+nums[i+1:]):
                    return a
