class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) == 0):
            return True

        if (len(s) % 2 != 0):
            return False 

        stack = []
        for c in s:
            match c:
                case '['|'{'|'(':
                    stack.append(c);
                case ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                case '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                case ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                case _:
                    return False

        if len(stack) != 0:
            return False
        
        return True