class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 0:
            return 0

        for c in tokens:
            if c == "+" or c == "-" or c == "*" or c == "/":
                second = stack.pop()
                first = stack.pop()

                if c == "+":
                    stack.append(first + second)
                elif c == "-":
                    stack.append(first - second)
                elif c == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(c))
        
        return stack[-1]