# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        subs = []
        res = 0

        while i < len(s):

            # if s[i] in subs, remove from left till one left
            while s[i] in subs and len(subs) > 1:
                del subs[0]

            if s[i] not in subs:
                subs.append(s[i])

            res = max(res, len(subs))

            i += 1

        return res