class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        A = [i for i in A]

        dp = [0 for i in range(len(A))]
        dp[0] = 1

        for i in range(1, len(A)):
            c = 0
            for j in range(i):
                if A[i] > A[j]:
                    c = max(c, dp[j])
            dp[i] = c + 1

        return dp[len(A) - 1]

if __name__ == "__main__":
    A = [ 1, 3, 5 ]
    obj = Solution()
    print(obj.lis(A))