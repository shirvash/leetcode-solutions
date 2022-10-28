from solutions.two_sum_II import Solution


def test_two_sum_II():
    solution = Solution()
    result = solution.twoSum(numbers=[2, 7, 11, 15], target=9)
    assert result == [1, 2]

    result = solution.twoSum(numbers=[2, 3, 4], target=6)
    assert result == [1, 3]

    result = solution.twoSum(numbers=[-1, 0], target=-1)
    assert result == [1, 2]
