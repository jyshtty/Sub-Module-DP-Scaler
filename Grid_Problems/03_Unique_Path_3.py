class Solution:
    def uniquePathsIII(self, grid):

        start, end = 0, 0
        block = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = [i, j]
                if grid[i][j] == 2:
                    end = [i, j]
                if grid[i][j] == 0:
                    block += 1

        ans = 0
        block += 1

        def dfs(start, count, ans):
            if start == end:
                if count == block:
                    ans += 1
                    return ans
                else:
                    return ans
            if count == block:
                return ans

            i, j = start
            if i > 0 and (grid[i - 1][j] == 0 or grid[i - 1][j] == 2):
                grid[i][j] = 1
                ans = dfs([i - 1, j], count + 1, ans)
                grid[i][j] = 0

            if j > 0 and (grid[i][j - 1] == 0 or grid[i][j - 1] == 2):
                grid[i][j] = 1
                ans = dfs([i, j - 1], count + 1, ans)
                grid[i][j] = 0

            if i < len(grid) - 1 and (grid[i + 1][j] == 0 or grid[i + 1][j] == 2):
                grid[i][j] = 1
                ans = dfs([i + 1, j], count + 1, ans)
                grid[i][j] = 0

            if j < len(grid[0]) - 1 and (grid[i][j + 1] == 0 or grid[i][j + 1] == 0):
                grid[i][j] = 1
                ans = dfs([i, j + 1], count + 1, ans)
                grid[i][j] = 0
            return ans

        return dfs(start, 0, ans)

if __name__ == "__main__":
    ls = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    obj = Solution()
    print(obj.uniquePathsIII(ls))










