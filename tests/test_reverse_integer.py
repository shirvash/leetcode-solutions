from solutions.reverse_integer import Solution

def test_reverse_integer():
    solution = Solution()
    result = solution.reverse(123)
    assert result == 321

    result = solution.reverse(-123)
    assert result == -321

    result = solution.reverse(120)
    assert result == 21