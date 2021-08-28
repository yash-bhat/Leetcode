"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        puncs = set(string.punctuation)
        puncs.add(" ")
        
        def check_alphabet(alph):
            if alph in puncs:
                return 0
            else:
                return 1
            
        filtered_s = list(filter(check_alphabet,s))
        s = ("".join(filtered_s)).lower()
        # print(s)
        
        
        if s==s[::-1]:
            return True
        else:
            return False
            
        #OR
        
        import re
        s = s.lower()
        s = re.sub('[\W_]+','',s)
        
        
        if s==s[::-1]:
            return True
        else:
            return False
