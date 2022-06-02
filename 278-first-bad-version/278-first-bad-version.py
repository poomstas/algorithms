# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #if isBadVersion(0):
            #return 0
        #if not isBadVersion(n):
            #return n
        L, R = 1, n
        M = (L+R)//2
        while L <= R:
            if isBadVersion(M):
                R = M-1
            else:
                L = M+1
            M = (L+R)//2
        return M+1
            
        