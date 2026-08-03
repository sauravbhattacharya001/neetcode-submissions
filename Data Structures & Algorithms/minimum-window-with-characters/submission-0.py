class Solution:

    def chartoindex(self, c: str) -> int:
        if ord(c) <= 90:
            return ord(c) - 65
        else:
            return ord(c) - 97 + 26

    def contains(self, s:List[int], t: List[int]) -> bool :
        for idx, c in enumerate(s):
            if t[idx] > c:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_count = [0] * 52
        s_count = [0] * 52
        left = 0
        right = 0
        maxlenstr = s
        found = False

        for c in t:
            t_count[self.chartoindex(c)] += 1

        for right in range(len(s)):
            s_count[self.chartoindex(s[right])] += 1

            last = ""
            while self.contains(s_count, t_count):
                last = s[left]
                s_count[self.chartoindex(s[left])] -= 1
                left += 1
            
            if last:
                s_count[self.chartoindex(last)] += 1
                left -=1

            if self.contains(s_count, t_count):
                found = True
                maxlenstr = s[left:right+1] if right - left + 1 < len(maxlenstr) else maxlenstr
        
        return maxlenstr if found else ""