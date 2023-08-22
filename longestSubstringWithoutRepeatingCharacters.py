class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLength = 0
        currentSubstringSet = set()
        l = 0

        for r in range(len(s)):
            if s[r] not in currentSubstringSet:
                currentSubstringSet.add(s[r])
                maxLength = max(maxLength, len(currentSubstringSet))
            else:
                while s[r] in currentSubstringSet:
                    currentSubstringSet.remove(s[l])
                    l += 1
                currentSubstringSet.add(s[r])

        return maxLength


# Main
def main():
    s = "ababccbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
