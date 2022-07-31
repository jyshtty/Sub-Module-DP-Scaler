#
#
# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     # def lcs(self, A, B, i, j, dp):
#     #     if i == -1 or j == -1:
#     #         return 0
#     #     if A[i] == B[j]:
#     #         dp[i][j] = [self.lcs(A, B, i - 1, j - 1, dp)]
#     #     else:
#     #         dp[i][j] = max(self.lcs(A, B, i, j - 1, dp), self.lcs(A, B, i - 1, j, dp))
#     #     return dp[i][j]
#     #
#     # def solve(self, A, B):
#     #     i = len(A) - 1
#     #     j = len(B) - 1
#     #     dp = [[-1] * (len(B)) for i in range(len(A))]
#     #     print(dp)
#     #     self.lcs(A, B, i, j, dp)
#     #     print(dp)
#
#         # @param A : string
#         # @param B : string
#         # @return an integer
#         # def lcs(self, A, B, i, j, dp):
#         #     if i == -1 or j == -1:
#         #         return 0
#
#         #     if A[i] == B[j]:
#         #         dp[i][j] = [self.lcs(A, B, i-1, j-1, dp)]
#         #     else:
#         #         dp[i][j] = max(self.lcs(A, B, i, j-1, dp), self.lcs(A, B, i-1, j, dp))
#
#         #     return dp[i][j]
#
#         # def solve(self, A, B):
#         #     i = len(A)-1
#         #     j = len(B)-1
#         #     dp = [[-1] * (len(B)-1) for i in range(len(A)-1)]
#
#         #     return self.lcs(A, B, i, j, dp)
#     def lcs(self, X, Y, m, n, dp):
#
#         if (m == 0 or n == 0):
#             return 0
#
#         if (dp[m][n] != -1):
#             return dp[m][n]
#
#         if X[m - 1] == Y[n - 1]:
#             dp[m][n] = 1 + self.lcs(X, Y, m - 1, n - 1, dp)
#             return dp[m][n]
#
#         dp[m][n] = max(self.lcs(X, Y, m, n - 1, dp), self.lcs(X, Y, m - 1, n, dp))
#         return dp[m][n]
#
#     def solve(self, A, B):
#         m = len(A)
#         n = len(B)
#         dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]
#         a = self.lcs(A, B, m, n, dp)
#         return a
#
#
# A = "aadaabaeeebabdddeabeaeadbaedeaaecabedcdddcaaadabdbbbcbbadcadeaebdbcbdaedeeaedabddebacecbbcbadadbbacbdeccdceddcebbceacbddeebeaecdcecaabeeddedaacdddeabcaaebbeddeaadcaebbaabacbcbbccdeebbdcdeabbcbbecdbaddbaaaaddcacbadaacdcabdcdeececceabacdabbcdabadbbdbddcdccedeeaedccdaaadbabebcceacaacedaccdddbecdbcaddacdebbdacddedaddcacdebedaeccaaccccbdabececdeecececadabeaadecdeabbdbe"
# B = "aadeecbeeadaedbeeabedbedaeedcdccdbeadcbeeeeecaadccecd"
# # |dbaccdcadbbeabeccdcdedcadaccbccadceaddbbaccaabaebecaceacbacccecceecccaacccaeaadbbabaeeeabbaabecadeedcbaeaceaeebaaeabaaebbededabecccedeadcbabbdcbdeededcdeacddecabebcabacddebbdcecdaececbbbbecabbbcdceaeedaaaaebdcdebcbaecbdaeabaebcdbceaebcaadaacebbadaecbbbdebccededebebaeddedcaceaabcceadccacebcdbbbaebadcbdecaaededcde"
# #
# # A = "beb"
# # B = "abc"
#
# obj = Solution()
# print(obj.solve(A, B))

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for i in range(m)]

    for i in range(n):
        if not obstacleGrid[0][i]:
            dp[0][i] = 1
        else:
            break

    for i in range(m):
        if not obstacleGrid[i][0]:
            dp[i][0] = 1
        else:
            break
    print(dp)

    for i in range(1, m):
        for j in range(1, n):
            if not obstacleGrid[i][j]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

print(uniquePathsWithObstacles([[0],[0]]))