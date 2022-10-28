# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        while x:
            y *= 10
            y += (x % 10)
            x //= 10
        if y <= 2 ** 31 - 1:
            return y * flag
        return 0
