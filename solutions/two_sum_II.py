# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        rel = {}
        for i, num in enumerate(numbers):
            if num in rel:
                return [rel[num] + 1, i + 1]
            rel[target - num] = i
