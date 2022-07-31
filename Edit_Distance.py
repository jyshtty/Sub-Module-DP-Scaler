class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        l1 = len(word1)
        l2 = len(word2)

        if not l1 or not l2:
            return max(l1, l2)

        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert_op = 1 + dp[i][j - 1]
                    delete_op = 1 + dp[i - 1][j]
                    replace_op = 1 + dp[i - 1][j - 1]
                    dp[i][j] = min(insert_op, delete_op, replace_op)
        print(dp)
        return dp[l1][l2]

    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word2), len(word1)
    #
    #     # empty word1 requires exactly len(word2) edits
    #     if not m or not n:
    #         return max(m, n)
    #
    #     # initialize dp with first col and row filled out
    #     # these are the empty string base cases
    #     dp = [[None] * (n + 1) for i in range(m + 1)]
    #     for i in range(n + 1):
    #         dp[0][i] = i
    #     for i in range(m + 1):
    #         dp[i][0] = i
    #
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             replace_cost = 0 if word1[j - 1] == word2[i - 1] else 1
    #             dp[i][j] = min(
    #                 # delete always requires an edit
    #                 dp[i][j - 1] + 1,
    #                 # insert always requires an edit
    #                 dp[i - 1][j] + 1,
    #                 # replace requires an edit
    #                 # iff chars are not matching
    #                 dp[i - 1][j - 1] + replace_cost
    #             )
    #     print(dp)
    #     return dp[m][n]
if __name__ == "__main__":
    a = "horse" #3 hor
    b = "ros" #1 r
    #
    # [0, 1, 2, 3, 4, 5]
    # [1, 1, 2, 3, 4, 5]

    obj = Solution()
    print(obj.minDistance(a,b))
    print("[[0, 1, 2, 3, 4, 5], [1, 1, 2, 2, 3, 4], [2, 2, 1, 2, 3, 4], [3, 3, 2, 2, 2, 3]]")