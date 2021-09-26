# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
# Example 4:
#
# Input: s = "([)]"
# Output: false
# Example 5:
#
# Input: s = "{[]}"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:

        par = {'(': ')', '[': ']', '{': '}'}
        res = []

        for i, p in enumerate(s):
            if i == 0 and p not in par:
                return False

            if i == 0:
                res.append(p)
                continue

            if p in par:
                res.append(p)
            elif len(res) > 0 and p == par[res[-1]]:
                res.pop()
            else:
                return False

        if len(res) == 0:
            return True
        else:
            return False