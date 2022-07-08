class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        output = []
        carry = 0
        
        for val_a, val_b in zip(reversed(a), reversed(b)):
            if val_a == '1':
                carry += 1
            if val_b == '1':
                carry += 1
                
            output.append(str(carry % 2)) # Simplified from last time
            carry //= 2
            
        if carry == 1:
            output.append('1')
            
        output.reverse()
        
        return ''.join(output)
            
        