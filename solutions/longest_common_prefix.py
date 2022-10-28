# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix = strs[0]
        while prefix != strs[-1][:len(prefix)]:
            prefix = prefix[:-1]
        return prefix
