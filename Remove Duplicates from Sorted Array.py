class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        res = list(set(nums))
        res.sort()
        
        for i,r in enumerate(res):
            nums[i] = r
        
        
        return len(res)
