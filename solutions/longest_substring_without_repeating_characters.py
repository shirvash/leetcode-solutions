# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, output, hash_map = 0, 0, {}
        for i, ch in enumerate(s):
            if (ch in hash_map) and (hash_map[ch] >= start):
                start = hash_map[ch] + 1
            else:
                output = max(output, i - start + 1)

            hash_map[ch] = i

        return output
