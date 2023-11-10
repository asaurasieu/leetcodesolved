class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        n = len(digits)

        #iterate through the list in reverse order 
        for i in range(n - 1, -1, -1):
            if digits[i] < 9: 
                digits[i] += 1
                return digits 
            digits[i] = 0 
        
        # if all the digits are 9, then add 1 to the beginning
        return [1] + digits 

        