class Solution:
    def groupAnagrams(self, strs):
        anagrams_map = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in anagrams_map:
                anagrams_map[key] = []

            anagrams_map[key].append(word)

        return list(anagrams_map.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
