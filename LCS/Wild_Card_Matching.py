class Solution:
    def isMatch(self, s, p):
        l1 = len(s)
        l2 = len(p)
        if not l1 and not l2:
            return True

        dp = [[True for i in range((l2 + 1))] for j in range((l1 + 1))]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if j == 0:
                    dp[i][j] = False
                elif i == 0:
                    for k in range(j):
                        if p[k] != '*':
                            dp[i][j] =  False
                            break
                elif i == 1 and j == 1 and (s[i-1] == p[j-1] or p[i-1] == '?'):
                    dp[i][j] == True
                elif p[j - 1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
        return dp[l1][l2]

if __name__ == "__main__":
    s = "ab"
    p = "?*"
    obj = Solution()
    print(obj.isMatch(s, p))