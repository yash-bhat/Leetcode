# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].



# BACKTRACK PROBLEM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        mapping = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl',
                   "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'}
        res = []

        def backtrack(path, index):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            cur_map = mapping[digits[index]]
            for char in cur_map:
                path.append(char)
                backtrack(path, index + 1)

                path.pop()

        backtrack([], 0)
        return res

