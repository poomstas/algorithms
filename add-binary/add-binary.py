class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        out = []
        carry = 0
       
        for val_a, val_b in zip(reversed(a), reversed(b)):
            carry += int(val_a=='1')
            carry += int(val_b=='1')
            out.append(str(carry % 2))
            carry //= 2
            
        if carry == 1:
            out.append('1')
        
        out.reverse()
        
        return ''.join(out)
            
        
            
        
        