class Solution:
    def productExceptSelf(self, nums):
        answer = []
        answer.append(1)

        for i in range(len(nums) - 1):
            answer.append(answer[i] * nums[i])

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix *= nums[i]

        return answer


if __name__ == "__main__":
    s = Solution()

    # Test 1 (Expected: [24, 12, 8, 6])
    nums1 = [1, 2, 3, 4]
    print("Test 1:", s.productExceptSelf(nums1))

    # Test 2 (Expected: [0, 0, 9, 0, 0])
    nums2 = [-1, 1, 0, -3, 3]
    print("Test 2:", s.productExceptSelf(nums2))
