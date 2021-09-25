Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.



class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s==s[::-1] or len(s) == 1:
            return s
        
        if s=='' or len(s)==0:
            return ''
        
        start = end = 0
        
        def expandonCenter(s,L,R):
            while(L>=0 and R<len(s) and s[L]==s[R]):
                L -= 1
                R += 1
            return R-L-1
            
            
        for i in range(len(s)):
            len1 = expandonCenter(s,i,i)
            len2 = expandonCenter(s,i,i+1)
            l = max(len1,len2)
            if (l>end-start):
                start = i - (l-1)//2
                end = i + l//2
                
        return s[start:end+1]
        
        
        
