from solutions.fizz_buzz import Solution


def test_fizz_buzz():
    solution = Solution()
    result = solution.fizzBuzz(15)
    assert result == \
           ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
