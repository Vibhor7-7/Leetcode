class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        while n != 1 and n not in seen:
            seen.add(n)
        
        # Calculate sum of squared digits
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            n = total
    
        return n == 1
