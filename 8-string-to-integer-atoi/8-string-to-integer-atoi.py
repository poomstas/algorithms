class Solution:
    def myAtoi(self, s: str) -> int:
        starting_indx = 0
        numchar = [str(num) for num in list(range(10))]
        
        if len(s)==0:
            return 0
        
        while starting_indx < len(s) and s[starting_indx] == ' ':
            starting_indx += 1
        
        if starting_indx >= len(s):
            return 0
        
        multiplier = 1
        if s[starting_indx] == '-':
            multiplier = -1
            starting_indx += 1
        elif s[starting_indx] == '+':
            starting_indx += 1
        elif s[starting_indx] not in [str(num) for num in list(range(10))]:
            return 0
        
        if starting_indx >= len(s) or s[starting_indx] not in numchar:
            return 0
        
        ending_indx = starting_indx + 1
        while ending_indx < len(s) and s[ending_indx] in numchar:
            ending_indx += 1
        
        value = 0
        digit = 1
        
        for char in reversed(s[starting_indx:ending_indx]):
            if char not in numchar:
                return self.process_clipping(value)
            value += digit * int(char)
            digit *= 10
            
        value *= multiplier
        
        return self.process_clipping(value)
    
    
    def process_clipping(self, value):
        if value < -2**31 :
            return -2**31
        elif value > 2**31-1:
            return 2**31-1
        else:
            return value
