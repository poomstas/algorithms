class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            number = 0
            for i, value in enumerate(reversed(digits)):
                number += value * 10**(i)
            number += 1
            return list(str(number))
        else:
            digits[-1] += 1
            return digits