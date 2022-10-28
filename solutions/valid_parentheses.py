# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        brackets = {')': '(', ']': '[', '}': '{'}
        open_bra = set(("(", "[", "{"))
        stack = []

        for sym in s:
            if sym in open_bra:
                stack.append(sym)
            elif stack and brackets[sym] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
