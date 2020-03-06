class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        print(nums1,nums2)
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        res = []
        
        if (l1<l2):
            for num in nums1:
                if num in nums2:
                    res.append(num)
                    idx = nums2.index(num)
                    nums2.pop(idx)
                
        else:
            for num in nums2:
                if num in nums1:
                    res.append(num)
                    idx = nums1.index(num)
                    nums1.pop(idx)
                    
        return res
