class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        hash_map = {}
        for num in nums:
            if num in hash_map:  
                hash_map[num] += 1
            else: 
                hash_map[num] =1 
        for num in nums: 
            if hash_map[num] == n: 
                return num
        
            

        