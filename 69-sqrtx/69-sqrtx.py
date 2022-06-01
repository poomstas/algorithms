class Solution:
    def mySqrt(self, x: int) -> int:
        int_sqrt = 0
        while True:
            squared = int_sqrt * int_sqrt
            if squared <= x:
                int_sqrt += 1
            else:
                return int_sqrt-1