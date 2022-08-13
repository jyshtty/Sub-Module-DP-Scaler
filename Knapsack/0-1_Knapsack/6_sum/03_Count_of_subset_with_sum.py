# only change from subset sum is
# initilisation True - 1, False - 0
# change or to + in dp expression.

class Solution:
    def solve(self, A, target):
        n = len(A)
        dp = [[0 for j in range(target + 1)] for i in range(n + 1)]  # same as Knapsack
        for j in range(target + 1):
            dp[0][j] = 0
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0 and j != 0:
                    dp[0][j] = False
                elif j == 0:
                     dp[i][0] = True
                else:
                    if j >= A[i - 1]:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - A[i - 1]]  # pick or un-pick
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp[n][target]

if __name__ == "__main__":
    nums = [2,3,5,6,8,10]
    target = 10
    obj = Solution()
    print(obj.solve(nums, target))