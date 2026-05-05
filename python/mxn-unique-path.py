# Given MxN array find all possible way you can go from top-left corner
# to the bottom-right assuming you can only go to right or down at any step.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
            
        
