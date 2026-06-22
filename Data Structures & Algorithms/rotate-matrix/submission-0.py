class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for x in range(len(matrix)):
            for y in range(x + 1, len(matrix[0])):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        print(matrix)
        for idx, lst in enumerate(matrix):
            matrix[idx] = reversed(lst)

        
