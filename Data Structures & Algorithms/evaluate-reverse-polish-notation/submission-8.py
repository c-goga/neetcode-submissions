class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        start = 0
        for token in tokens:
            print(stack, start)
            number = False
            match token:
                case '+':
                    stack[start] = stack[start] + stack.pop()
                case '-':
                    stack[start] = stack[start] - stack.pop()
                case '*':
                    stack[start] = stack[start] * stack.pop()
                case '/':
                    stack[start] = int(stack[start] / stack.pop())
                case _:
                    number = True
                    stack.append(int(token))
                    if len(stack) > 2:
                        start += 1
            if not number:
                if start > 0:
                    start -= 1

        return stack[start]