"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #remove any punctuation
        def removePunct(inp):
            punc = [',', '?', ':', ' ', '!','.','@']

            if(inp in punc):
                return False
            else:
                returan True

        s = list(filter(removePunct, s))
        s = "".join(map(str,s))
        
        print(s)
        
        if s.lower() == s[::-1].lower():
            return 1
        else:
            return 0
