class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # find possible row
        l, r = 0, rows - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        else:
            return False

        # binary search inside that row
        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False