class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in range(1, len(strs)):
            while prefix != "":
                if strs[i][: len(prefix)] != prefix:
                    prefix = prefix[:-1]
                else:
                    break
        return prefix


if __name__ == "__main__":
    # example
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # expected "fl"
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))  # expected ""
