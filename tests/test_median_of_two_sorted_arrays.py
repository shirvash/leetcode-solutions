from solutions.median_of_two_sorted_arrays import Solution


def test_median_of_two_sorted_arrays():
    solution = Solution()
    result = solution.findMedianSortedArrays([1, 3], [2])
    assert result == 2.0

    result = solution.findMedianSortedArrays([1, 2], [3, 4])
    assert result == 2.5

