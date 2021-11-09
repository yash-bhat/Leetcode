# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


# O(n) but takes more time
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        res = 0

        for i in range(1, len(height)):
            r = max(height[i:])

            diff = min(l, r) - height[i - 1]
            if diff > 0:
                res += diff

            l = max(height[:i])

        return res

# lesser time
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]

        return res



