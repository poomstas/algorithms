class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carryover = 0
        answer = []
        
        for val_a, val_b in zip(reversed(a), reversed(b)):
            if val_a == '1':
                carryover += 1
            if val_b == '1':
                carryover += 1
            
            if carryover % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carryover //= 2             # Nice trick to learn. Figure out what this does.
            
        if carryover == 1:              # Check for carry over one last time, after the loop
            answer.append('1')
            
        answer.reverse()
        
        return ''.join(answer)
