# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        l = len(merged)
        if len(merged) % 2 == 0:
            one = merged[int(l / 2 - 1)]
            two = merged[int(l / 2)]
            median = (one + two) / 2

        else:
            median = merged[int(l / 2)]
        return median
