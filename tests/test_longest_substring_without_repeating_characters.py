from solutions.longest_substring_without_repeating_characters import Solution


def test_fizz_buzz():
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s="abcabcbb")
    assert result == 3

    result = solution.lengthOfLongestSubstring(s="bbbbb")
    assert result == 1

    result = solution.lengthOfLongestSubstring(s="pwwkew")
    assert result == 3
