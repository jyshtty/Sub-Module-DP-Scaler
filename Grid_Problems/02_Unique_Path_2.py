class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        if obstacleGrid[0][0] == 1:
            return 0

        l = len(obstacleGrid)
        b = len(obstacleGrid[0])
        dp = [[1 for j in range(b)] for i in range(l)]

        # Resetting dp's 0th col to 1 if that block has obstacle.
        flag = 0
        for i in range(l):
            if flag == 1:
                dp[i][0] = 0
                continue

            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                flag = 1

        # Resetting dp's 0th row to 1 if that block has obstacle.
        flag = 0
        for j in range(b):
            if flag == 1:
                dp[0][j] = 0
                continue

            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                flag = 1

        for i in range(1, l):
            for j in range(1, b):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[l - 1][b - 1]

if __name__ == "__main__":
    list = [[0,0],[1,1],[0,0]]
    obj = Solution()
    print(obj.uniquePathsWithObstacles(list))