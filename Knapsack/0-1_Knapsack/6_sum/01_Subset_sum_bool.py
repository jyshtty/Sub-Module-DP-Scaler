# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
class Solution:
    def solve(self, A, target):
        n = len(A)
        dp = [[0 for j in range(target + 1)] for i in range(n + 1)]  # same as Knapsack
        for j in range(target + 1):
            dp[0][j] = False
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0 and j != 0:
                    dp[0][j] = False
                elif j == 0:
                     dp[i][0] = True
                else:
                    if j >= A[i - 1]:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]  # pick or un-pick
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp[n][target]
