class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        l = len(merged)
        if len(merged) % 2 == 0:
            one = merged[int(l / 2 - 1)]
            print(one)
            two = merged[int(l / 2)]
            print(two)
            median = (one + two) / 2

        else:
            median = merged[int(l/2)]
        return median
solution = Solution()
result = solution.findMedianSortedArrays([1,3,5,7], [2,4,6])
print(f'result:\n{result}')
print('expected:\n4')