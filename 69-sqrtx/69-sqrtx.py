# Binary Search Solution
# O(Nlog(N)) time | O(1) space

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x

        L, R = 0, x
        M = (L + R)//2
        
        while L <= R:
            if M*M < x:
                L = M+1
            elif M*M > x:
                R = M-1
            elif M*M == x:
                break
            M = (L + R)//2      # The placement of this matters. Work through the iters by hand.
        return M        
