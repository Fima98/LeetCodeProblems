class Solution:
    def topKFrequent(self, nums, k):
        freq_el = {}

        for num in nums:
            if num in freq_el:
                freq_el[num] += 1
            else:
                freq_el[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq_el.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result


if __name__ == "__main__":
    s = Solution()

    # Test 1 (Expected: [1, 2])
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    print("Test 1:", s.topKFrequent(nums1, k1))

    # Test 2 (Expected: [1])
    nums2, k2 = [1], 1
    print("Test 2:", s.topKFrequent(nums2, k2))
