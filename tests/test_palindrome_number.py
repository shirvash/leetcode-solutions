from solutions.palindrome_number import Solution


def test_palindrome_number():
    solution = Solution()
    result = solution.isPalindrome(121)
    assert result is True

    result = solution.isPalindrome(-121)
    assert result is False

    result = solution.isPalindrome(10)
    assert result is False
