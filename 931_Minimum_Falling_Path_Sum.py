class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][max(0, j-1):j+2])
        return min(matrix[-1])
solution = Solution()
matrix1 = [[2,1,3],[6,5,4],[7,8,9]]
matrix2 = [[-19,57],[-40,-5]]

print(solution.minFallingPathSum(matrix1))  # Output: 13
print(solution.minFallingPathSum(matrix2))  # Output: -59
