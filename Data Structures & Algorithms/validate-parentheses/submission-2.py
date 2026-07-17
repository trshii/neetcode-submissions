class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'}':'{', ')':'(', ']':'['}
        stack = []
        for char in s:
            if char not in paren:
                stack.append(char)
            elif char in paren:
                if not stack:
                    return False
                elif paren[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False

