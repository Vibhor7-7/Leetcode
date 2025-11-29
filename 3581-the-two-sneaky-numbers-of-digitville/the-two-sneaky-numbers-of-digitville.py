class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = []
        return_num = []
        for num in nums: 
            if num in seen:
                return_num.append(num)
            else: 
                seen.append(num)
        return return_num


        



        