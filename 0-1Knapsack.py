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
        dp = [[0 for j in range(C + 1)] for i in range(len(B) + 1)]

        for i in range(1, len(B) + 1):
            for j in range(1, C + 1):
                if i == 0: # no items
                    dp[i][j] = 0
                if j == 0: # knapsack threshold weight is 0
                dp[i][j] = dp[i - 1][j]. # no pick
                if j >= B[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - B[i - 1]] + A[i - 1]) # pick - index is always i-1 for B and A. For ex last element in weight array is B[i-1]
        return dp[len(B)][C]
    
    
 # unbounded Knapsack
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [[0 for j in range(C + 1)] for i in range(len(B) + 1)]

        for i in range(1, len(B) + 1):
            for j in range(1, C + 1):
                if i == 0: # no items
                    dp[i][j] = 0
                if j == 0: # knapsack threshold weight is 0
                dp[i][j] = dp[i - 1][j]. # no pick
                if j >= B[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j - B[i - 1]] + A[i - 1]) # pick - index is always i-1 for B and A. For ex last element in weight array is B[i-1]
        return dp[len(B)][C]



