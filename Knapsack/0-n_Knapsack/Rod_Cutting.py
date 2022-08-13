# Rod cutting
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        len_arr = [i for i in range(1, N + 1)]

        dp = [[0 for j in range(N + 1)] for i in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= len_arr[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j - len_arr[i - 1]] + A[i - 1])
        return dp[N][N]



