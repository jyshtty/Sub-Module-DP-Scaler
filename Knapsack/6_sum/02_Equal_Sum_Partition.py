# Backtracking

# class Solution:
#     def canPartition(self, nums):
#         total_sum = sum(nums)
#
#         def backtrack(index, sum):
#             if sum == (total_sum - sum):
#                 return True
#
#             if index >= len(nums):
#                 return False
#
#             return backtrack(index + 1, sum + nums[index]) or backtrack(index + 1, sum)
#
#         return backtrack(0, 0)


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

    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.solve(nums, total // 2)

if __name__ == "__main__":
    # nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
    nums = [2,13,1]
    obj = Solution()
    print(obj.canPartition(nums))
