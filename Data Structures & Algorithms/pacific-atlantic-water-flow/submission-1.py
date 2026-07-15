class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        reach = [[0] * COLS for _ in range(ROWS)]

        PACIFIC = 1
        ATLANTIC = 2

        def dfs(r, c, ocean, prev_height):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prev_height
                or reach[r][c] & ocean
            ):
                return

            reach[r][c] |= ocean
            current = heights[r][c]

            dfs(r + 1, c, ocean, current)
            dfs(r - 1, c, ocean, current)
            dfs(r, c + 1, ocean, current)
            dfs(r, c - 1, ocean, current)

        for r in range(ROWS):
            dfs(r, 0, PACIFIC, heights[r][0])
            dfs(r, COLS - 1, ATLANTIC, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, PACIFIC, heights[0][c])
            dfs(ROWS - 1, c, ATLANTIC, heights[ROWS - 1][c])

        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if reach[r][c] == 3:
                    result.append([r, c])

        return result