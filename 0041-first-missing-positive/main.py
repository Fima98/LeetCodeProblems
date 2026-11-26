class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        """ brute force O(n^2)
        for i in range(1, n+1):
            if i not in nums:
                return i
        """
        """ better way O(nlogn)
        if 1 not in nums:
                return 1
            nums = sorted(nums)
            for i in range(n-1):
                if i < n-1 and nums[i] > 0 and nums[i+1] != nums[i] + 1:
                    return nums[i] + 1
            return nums[-1] + 1
        """

        # for i in range(n):
        #     if not nums[i] >= 1 or not nums[i] <= n:
        #         continue
        #     a = nums[i]
        #     b = nums[a-1]

        #     if a-1 != i:
        #         nums[i] = b
        #         nums[a-1] = a
        #         if 1 <= b <= n and nums[b-1] != b:
        #             x = nums[b-1]
        #             nums[i] = x
        #             nums[b-1] = b
        #     else:
        #         continue

        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            a = nums[i]
            b = nums[a - 1]
            nums[i] = b
            nums[a - 1] = a

        print(nums)

        if nums[0] != 1:
            return 1

        for i in range(n-1):
            if nums[i+1] != (nums[i] + 1):
                return nums[i] + 1
        return n + 1


# -3 2 1 0 6 7
if __name__ == "__main__":
    s = Solution()
    # print(s.firstMissingPositive([7, 8, 9, 11, 12]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
