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

        return dp[len(A) - 1], dp



if __name__ == "__main__":
    A = [ 14, 24, 18, 46, 55, 53, 82, 18, 101, 20, 78, 35, 68, 9, 16, 93, 101, 85, 81, 28, 78 ]
    obj = Solution()
    print(obj.lis(A))
