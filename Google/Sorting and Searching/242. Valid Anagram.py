# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # or use own counter:
        # def counter(s):
        #     track = {}
        #     for char in s:
        #         if char in track:
        #             track[char] += 1
        #         else:
        #             track[char] = 1
        #     return track

        s_res = collections.Counter(s)
        t_res = collections.Counter(t)

        if s_res == t_res:
            return True
        else:
            return False
