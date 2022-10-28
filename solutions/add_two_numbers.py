from typing import Optional


# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    """Definition for singly-linked list from leetcode"""

    def __init__(self, val: int = 0, next=None, values=None):
        if values is None:
            values = []
        self.val = val
        self.next = next

        if values:  # this help to create ListNodes object easier without breaking the original logic
            self.imp(values)

    def export(self) -> list:
        """function take all nodes and return list of values"""
        tmp_node = self
        result = [tmp_node.val]
        while tmp_node.next:
            tmp_node = tmp_node.next
            result += [tmp_node.val]
        return result

    def imp(self, values: list) -> None:
        """function takes list and change self object to nodes
        with values from list"""
        tmp_node = None
        self.val = values[0]
        while len(values) > 1:
            tmp_node = ListNode(values.pop(), tmp_node)
        self.next = tmp_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
