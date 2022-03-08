class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            number = 1 # Start with 1 added. Same as starting with 0 and adding 1 later.
            for i, value in enumerate(reversed(digits)):
                number += value * 10**(i)
            return list(str(number))
        else:
            digits[-1] += 1
            return digits