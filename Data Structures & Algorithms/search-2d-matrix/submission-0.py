class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        for row in range(r):
            for col in range(c):
                if matrix[row][col] == target:
                    return True


        return False