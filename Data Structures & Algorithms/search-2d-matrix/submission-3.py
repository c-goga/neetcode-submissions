class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = 0
        while matrix[r][c] != target:
            print('r', r)
            print('c', c)
            print(matrix[r][c])
            print('size', len(matrix[r]))
            if r+1 < len(matrix) and matrix[r+1][c] <= target:
                r += 1
            elif c+1 < len(matrix[r]) and matrix[r][c+1] <= target:
                c += 1
            else:
                return False

            # if r >= len(matrix) or c >= len(matrix[0]):
            #     print('fail 2')
            #     return False
        
        return True