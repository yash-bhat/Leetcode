class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # print(len(nums))
        if (len(nums) == 0) or (len(nums) == 1):
            return 0
        
        count = {}
        
        for i,a in enumerate(nums):
            if a not in count.keys():
                count[a] = 0
            count[a] += 1
            if count[a] > 1:
                return 1
            
        return 0
