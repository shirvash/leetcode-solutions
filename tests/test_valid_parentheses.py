from solutions.valid_parentheses import Solution


def test_valid_parentheses():
    solution = Solution()

    result = solution.isValid('()[]{}({[]})')
    assert result is True

    result = solution.isValid('{[(])}')
    assert result is False