class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p, j = m-1, n-1
        
        for i in reversed(range(len(nums1))):
            if j < 0:
                break
            if p < 0:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                j -= 1
                continue
                
            P, I, J = nums1[p], nums1[i], nums2[j]
            
            if P < J:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                j -= 1
            else:
                nums1[p], nums1[i] = nums1[i], nums1[p]
                p -= 1
            
# Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.

'''
[4,5,6,0,0,0]
3
[1,2,3]
3
'''