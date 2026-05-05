# Given a graph find the number of connected sub-graphs
class Solution:
    def bfs(self, graph, start, visited, size):
        queue = deque([start])

        while queue:
            v = queue.popleft()

            if v in visited:
                continue
            visited.add(v)

            for n in range(size):
                if graph[v][n] != 0 and n not in visited:
                    queue.append(n)

        return visited

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = set()

        prov_count = 0
        for i in range(size):
            if i not in visited:
                visited = self.bfs(isConnected, i, visited, size)
                prov_count += 1

        return prov_count
