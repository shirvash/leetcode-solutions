from solutions.two_sum import Solution


def test_two_sum():
    solution = Solution()
    result = solution.twoSum(nums=[2, 7, 11, 15], target=9)
    assert result == [0, 1]
    result = solution.twoSum(nums=[3, 2, 4], target=6)
    assert result == [1, 2]
    result = solution.twoSum(nums=[3, 3], target=6)
    assert result == [0, 1]
