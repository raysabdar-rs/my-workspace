# Given a phone number find all possible letter combinations
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dial = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' }

        rv = []

        def dfs(i, stk):
            if i == len(digits):
                rv.append(''.join(stk))
                return
            for n in dial[int(digits[i])]:
                stk.append(n)
                dfs(i + 1, stk)
                stk.pop()

        dfs(0, [])
        return rv


