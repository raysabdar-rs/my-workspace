# Retrurn true if an integer is a palindrome
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        def palindrome(x):
            rv = 0
            while x > 0:
                rv = rv * 10 + x % 10
                x /= 10
            return rv

        print(palindrome(x))

        return x == palindrome(x)
        
