# Find the longest palindrome substring
class Solution(object):
    def palindrom(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rv = ''
        for i in range(len(s)):
            rv = max(rv, self.palindrom(s, i, i), self.palindrom(s, i, i+1), key=len)

        return rv
        
