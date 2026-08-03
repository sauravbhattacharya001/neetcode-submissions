class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        left = 0
        right = 0
        maxrep = 0
        most =0

        for right in range(len(s)):
            freq[s[right]] += 1
            most = freq[s[right]] if most < freq[s[right]] else most

            while right - left + 1 - most > k:
                freq[s[left]] -= 1
                left += 1

            maxrep = right - left + 1  if right - left + 1 > maxrep else maxrep
        return maxrep


