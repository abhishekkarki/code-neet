# https://neetcode.io/problems/rotting-fruit
# Medium

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        m, n = len(grid), len(grid[0])

        queue = deque()
        
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        minu = 0
        while queue:
            i, j, minu = queue.popleft()
            if i > 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append((i-1, j, minu+1))
            if i < m-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append((i+1, j, minu+1))
            if j > 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                queue.append((i, j-1, minu+1))
            if j < n-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                queue.append((i, j+1, minu+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minu