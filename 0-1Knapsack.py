class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [[0 for i in range(C + 1)] for j in range(len(B) + 1)]

        for i in range(1, len(B) + 1):
            for j in range(1, C + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= B[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - B[i - 1]] + A[i - 1])
        return dp[len(B)][C]