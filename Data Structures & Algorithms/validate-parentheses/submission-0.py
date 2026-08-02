class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack[-1] == "[" and not c == "]":
                return False
            elif stack[-1] == "{" and not c == "}":
                return False
            elif stack[-1] == "(" and not c == ")":
                return False
            else:
                stack.pop()
        
        return len(stack) == 0
