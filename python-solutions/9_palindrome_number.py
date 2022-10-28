class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        length = len(x)
        for i in range(int(length / 2)):
            if x[i] == x[length - i - 1]:
                pass
            else:
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        return x == x[::-1]