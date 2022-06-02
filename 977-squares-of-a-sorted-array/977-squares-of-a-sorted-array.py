class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R = 0, n-1
        output = [None] * n
        for i in range(n):
            Lval, Rval = nums[L], nums[R]
            if abs(Lval) > abs(Rval):
                output[n-i-1] = Lval**2
                L += 1
            else:
                output[n-i-1] = Rval**2
                R -= 1
        return output
            
                
        