class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #if the exponent is 0, the result is 1
        if n == 0:
            return 1

        #if the exponent is negative, the base is inverted (1/x)
        if n < 0:
            x = 1 / x
            n = -n
        
        #the exponent is even
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half

        #the exponent is negative
        else:
            return x * self.myPow(x, n-1)
        
    
