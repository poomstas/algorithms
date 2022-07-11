class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:] # Not the most optimal solution because it uses O(m) space, but it works.
        i, j = 0, 0
        
        for pointer in range(m + n):
            a = nums1_copy[i] if i < m else float('inf')
            b = nums2[j] if j < n else float('inf')
            nums1[pointer] = min(a, b)
            
            if a < b:
                i += 1
            elif a == b:
                i += 1
            else:
                j += 1
            
