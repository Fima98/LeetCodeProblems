class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i - k])

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
