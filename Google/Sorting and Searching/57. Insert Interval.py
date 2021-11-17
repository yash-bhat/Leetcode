# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Example 3:

# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
# Example 4:

# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
# Example 5:

# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        
        for i,interval in enumerate(intervals):
            if (newInterval[1] < interval[0]):
                # no overlap , first place new interval
                res.append(newInterval)
                return res + intervals[i:]
            elif (newInterval[0] > interval[1]):
                # no overlap on interval, thus add interval
                # but check new interval against rest later
                res.append(interval)
                
            else:
                # overlaps!
                newInterval = [min(interval[0],newInterval[0]),
                        max(interval[1],newInterval[1])]
                
            if i+1 == len(intervals):
                res.append(newInterval)
                
                
                
                
                
        return res
            
