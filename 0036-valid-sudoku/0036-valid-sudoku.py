class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # 각 행에서 중복된 값이 있는지 체크
        # for row in board:
        #     row_num = [num for num in row if num != "."]
        #     if len(row_num) != len(set(row_num)):
        #         return False
        
        # # 각 열에서 중복된 값이 있는지 체크
        # for col in range(len(board[0])):
        #     col_num = [board[row][col] for row in range(len(board[0])) if board[row][col] != "."]
        #     if len(col_num) != len(set(col_num)):
        #         return False
        
        # # 3*3 box에서 중복된 값이 있는지 체크
        # for box_row in range(0, 9, 3):
        #     for box_col in range(0, 9, 3):
        #         box_num = []
        #         for row in range(box_row, box_row + 3):
        #             for col in range(box_col, box_col + 3):
        #                 if board[row][col] != ".":
        #                     box_num.append(board[row][col])
        #         if len(box_num) != len(set(box_num)):
        #             return False
        
        # return True

        boardMap = collections.defaultdict(list)

        for row in range(9):
            for col in range(9):
                char = board[row][col]
                if char != ".":
                    for pos in boardMap[char]:
                        # //은 floor-division이고 array나 list에서 어떤 범주 안에 들어가는지 계산할 때 이렇게 쓰일 수 있다
                        if (pos[0] == row) or (pos[1] == col) or (pos[0]//3 == row//3 and pos[1]//3 == col//3):
                            return False
                boardMap[char].append([row, col])
        return True

        