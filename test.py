class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        mat = [[0 for i in range(n)] for j in range(n)]
        mat[0][0] = 1

        def backtrack(mat, i, j):
            if i == n - 1 and j == n - 1:
                mat[n - 1][n - 1] = 1
                return True
            a = False
            b = False
            if A[i][j] == 1:
                mat[i][j] = 1
                if i + 1 < n:
                    if backtrack(mat, i + 1, j):
                        return True

                if j + 1 < n:
                    if  backtrack(mat, i, j + 1):
                        return True
                mat[i][j] = 0

            else:
                return False
        backtrack(mat, 0, 0)
        return mat

obj = Solution()
print(obj.solve([[1, 0], [1, 1]]))
