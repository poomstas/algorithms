class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        M = (L+R)//2
        
        while L <= R:
            if nums[M] < target:
                L = M+1
            elif nums[M] > target:
                R = M-1
            else:
                return M
            M = (L+R)//2
        return -1