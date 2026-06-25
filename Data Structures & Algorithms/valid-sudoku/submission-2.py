class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                x = board[i][j]
                if x == ".":
                    continue

                if x in row[i] or x in col[j] or x in box[j // 3 + (i // 3 * 3)]:
                    print(row)
                    print(col)
                    print(box)
                    return False
                else:
                    row[i].add(x)
                    col[j].add(x)
                    box[j // 3 + (i // 3 * 3)].add(x)

        return True


