class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0" or grid[i][j] == "V":
                return
            
            grid[i][j] = "V"

            dfs(i-1, j, grid)
            dfs(i+1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)

            return

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j,grid)

        return res

        
