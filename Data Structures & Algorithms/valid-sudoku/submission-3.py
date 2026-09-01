class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for i in range(len(board)):
            seen = set()
            for value in board[i]:
                if value == ".":
                    continue
                if value in seen :
                    return False
                seen.add(value)
        # check column
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                value = board[j][i]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
         # check 3vs3 box 
        for box_row in range(3): # get which box_row
            for box_col in range(3):# get which box_column
                #initialize the actual box and row values and set to check duplicates
                actual_row = box_row * 3 
                actual_col = box_col * 3 
                seen = set() 
                # now get the value in box 
                for row in range(3):
                    for col in range(3):
                        value = board[actual_row + row][actual_col + col]
                        # ignore dot value
                        if value == ".":
                            continue
                        # check duplicate
                        if value in seen:
                            return False
                        seen.add(value)
        return True
        