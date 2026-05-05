# Return true if the parentheses sequence is valid
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['(', '{', '[']:
                stk.append(c)
            else:
                if not stk:
                    return False
                ch = stk.pop()
                if c == ')' and ch != '(':
                    return False
                if c == '}' and ch != '{':
                    return False
                if c == ']' and ch != '[':
                    return False
        if stk:
            return False
        return True



        
