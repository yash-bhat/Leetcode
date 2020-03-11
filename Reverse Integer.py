"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        if x<0:
            neg = 1
            
        res = list(map(int, str(abs(x))))
        
        res = res[::-1]
        
        res = "".join(map(str, res))
        res = int(res)
        
        # print(res,type(res))
        
        if res > (2**31)-1:
            return 0
        
        
        if neg:
            return -(res)
        else:
            return (res)
