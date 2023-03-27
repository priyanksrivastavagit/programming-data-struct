class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        good_numbers = {'2','5','6','9'}
        bad_numbers = {'3','4','7'}
        counter = 0
        
        for elem in range(1, n+1):
            
            uniq_digits = set(str(elem))
            
            if (uniq_digits & good_numbers) and not(uniq_digits & bad_numbers):
                counter += 1

            
        return counter
