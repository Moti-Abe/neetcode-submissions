class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        isValid = True
        for i in range(row):
            arr1 = []
            arr2 = []
            for j in range(col):
                if board[i][j].isdigit():
                    arr1.append(board[i][j])
                
                if board[j][i].isdigit():
                    arr2.append(board[j][i])
            
            if len(arr1) != len(set(arr1)):
                isValid = False
            if len(arr2) != len(set(arr2)):
                isValid = False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        val = board[r + i][c + j]
                        if val.isdigit():
                            box.append(val)
                if len(box) != len(set(box)):
                    isValid = False

        return isValid
