class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        max_len = 0

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            max_len = max(max_len, dp[i][j])

        return max_len