from solutions.zigzag_conversion import Solution


def test_zigzag_conversion():
    solution = Solution()

    result = solution.convert(s='PAYPALISHIRING', numRows=4)
    assert result == 'PINALSIGYAHRPI'

    result = solution.convert(s='PAYPALISHIRING', numRows=3)
    assert result == 'PAHNAPLSIIGYIR'

    result = solution.convert(s='PAYPALISHIRING', numRows=5)
    assert result == 'PHASIYIRPLIGAN'
