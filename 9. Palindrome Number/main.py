class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x != 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num

    def isPalindromeStr(self, x):
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [121, -121, 10, 12321]
    results = {x: solution.isPalindrome(x) for x in test_cases}
    print(results)  # Output: {121: True, -121: False, 10: False, 12321: True}
