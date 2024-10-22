# https://neetcode.io/problems/pacific-atlantic-water-flow
# Medium

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()
        pacific_reach = set()
        atlantic_reach = set()

        def dfs(i, j, pac=True):
            if pac:
                if (i, j) in pacific_visited: return
                pacific_visited.add((i, j))
                pacific_reach.add((i, j))
            else:
                if (i, j) in atlantic_visited: return
                atlantic_visited.add((i, j))
                atlantic_reach.add((i, j))
            if i > 0 and heights[i-1][j] >= heights[i][j]:
                dfs(i-1, j, pac)
            if i < m-1 and heights[i+1][j] >= heights[i][j]:
                dfs(i+1, j, pac)
            if j > 0 and heights[i][j-1] >= heights[i][j]:
                dfs(i, j-1, pac)
            if j < n-1 and heights[i][j+1] >= heights[i][j]:
                dfs(i, j+1, pac)
            return
        
        for i in range(m):
            dfs(i, 0, True)
            dfs(i, n-1, False)
        for j in range(1, n):
            dfs(0, j, True)
            dfs(m-1, j-1, False)
        
        res = []
        for pi, pj in pacific_reach:
            if (pi, pj) in atlantic_reach:
                res.append([pi, pj])
        return res