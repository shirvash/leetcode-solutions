from solutions.longest_common_prefix import Solution


def test_longest_common_prefix():
    solution = Solution()
    result = solution.longestCommonPrefix(strs=['flower', 'flow', 'flight'])
    assert result == 'fl'

    result = solution.longestCommonPrefix(strs=["dog", "racecar", "car"])
    assert result == ''
