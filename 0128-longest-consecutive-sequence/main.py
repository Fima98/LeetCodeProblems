class Solution:
    def longestConsecutive(self, nums):

        max_len = 0
        current_len = 1

        numset = set(nums)

        for num in numset:
            if num - 1 not in numset:
                next = num + 1
                while next in numset:
                    current_len += 1
                    next += 1

                max_len = max(current_len, max_len)
                current_len = 1

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
