class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = 0
        while matrix[r][c] != target:
            if r+1 < len(matrix) and matrix[r+1][c] <= target:
                r += 1
            elif c+1 < len(matrix[r]) and matrix[r][c+1] <= target:
                c += 1
            else:
                return False

        return True