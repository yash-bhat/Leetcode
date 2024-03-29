# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Lengthy approach - sorting - Olog(n) * n
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        i = 0
        res = []
        
        while i < len(intervals)-1:
            first = intervals[i]
            second = intervals[i+1]
            
            if first[1] >= second[0] and first[1] <= second[1]:
                temp = [first[0],second[1]]
                del intervals[i]
                del intervals[i]
                intervals.insert(i,temp)
            
            elif first[1] >= second[0] and first[1] > second[1]:
                temp = [first[0],first[1]]
                del intervals[i]
                del intervals[i]
                intervals.insert(i,temp)
                
            else:
                i += 1
                
        return intervals
        
# concise - sorting - Olog(n) * n       
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        res = []
        
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
                
            else:
                res[-1][1] = max(res[-1][1],interval[1])
                
                
        return res
