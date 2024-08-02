class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reverse = 0 
        temp_var = x 

        while temp_var > 0: 

            last_number = temp_var % 10
            reverse = reverse * 10 + last_number 
            temp_var //= 10

        return x == reverse 