class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        run_length = 1 
        total = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1]-1:
                run_length+=1
            else: 
                run_length=1 
            total+= run_length
        return total
