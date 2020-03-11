"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        import collections
        
        check = list(s)
        
        count = collections.Counter(s)
        print(count)
        i=-1
        
        for k,v in count.items():
            i += 1
            if v == 1:
                return check.index(k)
            
        return -1
        
