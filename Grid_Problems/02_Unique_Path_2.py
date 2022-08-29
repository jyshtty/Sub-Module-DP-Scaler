class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        l = len(obstacleGrid)
        b = len(obstacleGrid[0])
        dp = [[1 for j in range(b)] for i in range(l)]


        # Resetting dp's 0th col to 1 if that block has obstacle.
        for i in range(l):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0

        # Resetting dp's 0th row to 1 if that block has obstacle.
        for j in range(b):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0

        for i in range(1, l):
            for j in range(1, b):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[l - 1][b - 1]

if __name__ == "__main__":
    grid = [[0,1],[0,0]]
    obj = Solution()
    print(obj.uniquePathsWithObstacles(grid))
