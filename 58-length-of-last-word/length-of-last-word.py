class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        alpha_count = 0 
        right = len(s)-1
        while right>=0: 
            if s[right].isalpha(): 
                alpha_count+=1
            elif alpha_count>0: 
                break
            right-=1 
        return alpha_count




        