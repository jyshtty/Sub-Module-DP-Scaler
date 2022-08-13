class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        A, B, C = B, C, A
        dp = [[0 for i in range(A + 1)] for j in range(len(C) + 1)]

        for index in range(1, len(C) + 1):
            for j in range(1, A + 1):
                dp[index][j] = dp[index - 1][j]
                if j >= B[index - 1]:
                    dp[index][j] = max(dp[index][j], dp[index][j - C[index - 1]] + B[index - 1])
        return dp[len(C)][A]

# A = 10
# B = [ 5 ]
# C = [ 10 ]

A, B, C = B, C, A

print(A)
print(B)
print(C)
