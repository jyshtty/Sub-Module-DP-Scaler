# # Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

# # Also given an integer C which represents knapsack capacity.

# # Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

# # NOTE:

# # You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


#  A = [60, 100, 120]
#  B = [10, 20, 30]
#  C = 50
    
#  o/p - 220



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [[0 for i in range(C + 1)] for j in range(len(B) + 1)]

        for i in range(1, len(B) + 1):
            for j in range(1, C + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= B[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - B[i - 1]] + A[i - 1])
        return dp[len(B)][C]