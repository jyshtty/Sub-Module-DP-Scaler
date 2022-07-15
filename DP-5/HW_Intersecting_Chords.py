class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        dp = [-1 for i in range(A + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, A + 1):
            ans = 0
            for j in range(i):
                ans += dp[j] * dp[i - 1 - j]
            dp[i] = ans
        return dp[A]


if __name__ == "__main__":
    A = 3
    obj = Solution()
    print(obj.chordCnt(A))