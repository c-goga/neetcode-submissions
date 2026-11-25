class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # two hash tables, one for rows, one for columns
        # check if 3x3 area by comparing distance of vertex
        rows = defaultdict(list)
        cols = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if i in rows[board[i][j]] or j in cols[board[i][j]]:
                        return False
                    rows[board[i][j]].append(i)
                    cols[board[i][j]].append(j)
        groups = [[0,1,2], [3,4,5], [6,7,8]]
        for key in rows:
            for i in range(len(rows[key]) - 1):
                if rows[key][i+1] - rows[key][i] < 3 and cols[key][i+1] - cols[key][i] < 3:
                    for group in groups:
                        for group2 in groups:
                            if (rows[key][i+1] in group and rows[key][i] in group) and (cols[key][i+1] in group2 and cols[key][i] in group2):
                                return False
            
        return True

        
