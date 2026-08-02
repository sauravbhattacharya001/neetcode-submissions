class Solution:

    def diff (self, a:int, b:int):
        if a-b < 0:
            return b-a
        return a-b

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if (s[left].isdigit() and not s[right].isdigit() or 
               not s[left].isdigit() and s[right].isdigit()):
                return False

            if (s[left] != s[right] and
                self.diff( ord(s[left]) , ord(s[right]) ) != 32
            ):
                return False

            left +=1
            right -=1

        return True
