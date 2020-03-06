"""

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
                l = len(digits)
                for i in range(l-1,-1,-1):
                    print(i)
                    if i == 0:
                        if digits[i] == 9:
                            digits[i] = 0
                            return [1]+digits
                        else:
                            digits[i] += 1
                            return digits
                    elif digits[i] == 9:
                        digits[i] = 0
                    else:
                        digits[i] += 1
                        return digits
        
        # OR
        # a = "".join(map(str,digits))
        # b = str(int(a) + 1)
        # return list(b)
