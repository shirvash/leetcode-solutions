# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> dict[int, list[str]]:
        hashmap = {}
        result = ''
        counter = 0
        for _ in range(numRows):
            hashmap[_] = []
        for i in range(int(len(s) / numRows) + 1):
            try:
                for j in range(numRows):
                    hashmap[j].append(s[counter])
                    counter += 1
                for k in range(numRows - 2, 0, -1):
                    hashmap[k].append(s[counter])
                    counter += 1
            except IndexError:
                pass
        for key in hashmap:
            result += ''.join(hashmap[key])
        return result
