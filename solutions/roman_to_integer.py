# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        summ = 0
        prev = None
        prev_dig = 0
        rels = {'I': 1,
                'V': 5,
                'IX': 9,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        for el in s:
            dig = rels[el]
            if prev_dig < dig and prev:
                dig = rels[el] - rels[prev] - prev_dig
            summ += dig
            prev = el
            prev_dig = dig
        return summ
