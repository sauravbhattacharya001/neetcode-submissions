class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        myset = set()

        left = 0
        right = 0

        for right in range(len(s)):
            if s[right] not in myset:
                myset.add(s[right])

            else:
                while s[right] in myset:
                    myset.remove(s[left])
                    left += 1

                myset.add(s[right])

            maxlen = right - left + 1 if right - left + 1 > maxlen else maxlen
        return maxlen

