class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            ROW, COL = q.popleft()
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                R = ROW + i
                C = COL + j
            
                if R < 0 or C < 0 or R == ROWS or C == COLS or grid[R][C] != 2147483647:
                    continue
                
                grid[R][C] = grid[ROW][COL] + 1
                q.append((R,C))