# Given a string s, return the length of the longest substring that contains at most two distinct characters.
#
#
#
# Example 1:
#
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:
#
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of English letters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        L = len(s)

        if len(s) < 3:
            return L

        l, r = 0, 0

        res = 2

        track = {}

        while r < L:
            track[s[r]] = r
            r += 1

            if len(track) > 2:
                del_idx = min(track.values())
                del track[s[del_idx]]

                l = del_idx + 1

            res = max(res, r - l)

        return res
