from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruit_count = 0

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fruit_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        cnt = 0

        while q and fruit_count > 0:
            for _ in range(len(q)):
                ROW, COL = q.popleft()

                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row = ROW + i
                    new_col = COL + j

                    if (
                        new_row < 0 or
                        new_row == len(grid) or
                        new_col < 0 or
                        new_col == len(grid[0]) or
                        grid[new_row][new_col] != 1
                    ):
                        continue

                    grid[new_row][new_col] = 2
                    fruit_count -= 1
                    q.append((new_row, new_col))

            cnt += 1

        return cnt if fruit_count == 0 else -1