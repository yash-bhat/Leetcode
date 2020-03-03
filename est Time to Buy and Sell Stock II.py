class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]):
                maxProf += prices[i] - prices[i-1]
                
        return maxProf
