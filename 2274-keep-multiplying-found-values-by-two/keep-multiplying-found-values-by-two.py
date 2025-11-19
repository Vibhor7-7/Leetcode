class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        for num in nums: 
            if original in nums: 
                original = original*2 
        return original 
        