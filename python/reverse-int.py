# Give a signed integer, make it reversed
class Solution:
    def reverse(self, x: int) -> int:
        rv = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            rv += x % 10
            rv *= 10
            x //= 10

        rv //= 10
        if rv > 2**31 or rv < -2**31:
            return 0

        return sign*rv

        
