class Solution:
    def isAlienSorted(self, words, order):
        indexes = {}
        for i, char in enumerate(order):
            indexes[char] = i

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j >= len(w2):
                    return False
                if w1[j] != w2[j]:
                    if indexes[w1[j]] > indexes[w2[j]]:
                        return False
                    break

        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1 (Output: True)
    words1 = ["hello", "leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    print("Test 1:", sol.isAlienSorted(words1, order1))

    # Test 2 (Output: False)
    words2 = ["word", "world", "row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    print("Test 2:", sol.isAlienSorted(words2, order2))

    # Test 3 (Output: False)
    words3 = ["apple", "app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"
    print("Test 3:", sol.isAlienSorted(words3, order3))
