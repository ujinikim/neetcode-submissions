class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 0, 0
        # 0 means nothing
        # 1 means just row
        # 2 means just column
        # 3 means both
        rowZero = 0
        colZero = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0 or j == 0:
                        if i == 0:
                            rowZero = 1
                        if j == 0:
                            colZero = 1
                    else:
                        matrix[0][j], matrix[i][0] = 0, 0
        print(matrix)
        print(rowZero)
        print(colZero)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                
        if rowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if colZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        



        