# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
#
# Input: nums = [1]
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(nums, start):
            l = start
            r = len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # find peak
        L = len(nums)
        i = L - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i > -1:

            j = L - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        rev(nums, i + 1)