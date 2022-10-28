from solutions.add_two_numbers import Solution, ListNode


def test_add_two_numbers():
    l1 = ListNode(0, None, [2, 4, 3])
    l2 = ListNode(0, None, [5, 6, 4])

    l3 = ListNode(0)
    l4 = ListNode(0)

    l5 = ListNode(0, None, [9, 9, 9, 9, 9, 9, 9])
    l6 = ListNode(0, None, [9, 9, 9, 9])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assert result.export() == [7, 0, 8]

    result = solution.addTwoNumbers(l3, l4)
    assert result.export() == [0]

    result = solution.addTwoNumbers(l5, l6)
    assert result.export() == [8, 9, 9, 9, 0, 0, 0, 1]
