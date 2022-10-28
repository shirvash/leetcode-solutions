from solutions.roman_to_integer import Solution


def test_roman_to_integer():
    solution = Solution()
    result = solution.romanToInt(s="III")
    assert result == 3

    result = solution.romanToInt(s="LVIII")
    assert result == 58

    result = solution.romanToInt(s="MCMXCIV")
    assert result == 1994
