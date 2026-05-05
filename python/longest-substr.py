# Find the longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ln = 0
        l = []
        mxlen = 0
        mxstr = ''
        for ch in s:
            if ch not in l:
                l.append(ch)
                mxlen = max(mxlen, len(l))
                mxstr = ''.join(l)
            else:
                while ch in l:
                    l.pop(0)
                l.append(ch)
        #print(mxstr)
        return mxlen
