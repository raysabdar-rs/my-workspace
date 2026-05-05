# Given a matrix of 0's and 1's find the number of islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        """
        deq = deque([])
        visited = []

        def bfs(a, b):

            if (a,b) in visited:
                return None

            deq.append((a, b))

            while deq:
                p = deq.popleft()
                if p in visited:
                    continue

                i = p[0]
                j = p[1]

                if grid[i][j] == "1":
                    visited.append((i, j))
                    if i < m-1 and grid[i+1][j] == "1":
                        deq.append((i+1, j))
                    if j < n-1 and grid[i][j+1] == "1":
                        deq.append((i, j+1))
                    if i > 0 and grid[i-1][j] == "1":
                        deq.append((i-1, j))
                    if j > 0 and grid[i][j-1] == "1":
                        deq.append((i, j-1))

            return 1

        """
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
                return

            grid[i][j] = 'X'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i , j)
                    cnt += 1

        return cnt
        

