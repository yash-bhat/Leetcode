# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = 0
        r = len(nums) - 1
        res = []
        found_l, found_r = 0, 0

        while l <= r: # check equal if one occurence of target

            if nums[l] == target and not found_l:
                res = [l] + res
                found_l = 1

            if nums[r] == target and not found_r:
                res.append(r)
                found_r = 1

            if found_l and found_r:
                return res

            if not found_l:
                l += 1

            if not found_r:
                r -= 1

        return [-1, -1]
