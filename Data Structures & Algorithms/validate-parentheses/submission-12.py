class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        
        stack = []

        for i in s:
            print(i)
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
                continue
        
            if len(stack) == 0:
                print('empty stack + ending')
                return False

            if i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0