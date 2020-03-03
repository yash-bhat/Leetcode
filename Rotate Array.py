class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k == l or (k == 0):
            return nums
        
        if (l>k):
            r = l - k
        else:
            r = 2*l - k 
        
        for i in range(r):
            nums.append(nums.pop(0))
