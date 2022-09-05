class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dpsleep = [0] * (A + 1)
        dppizza = [0] * (A + 1)
        dptv = [0] * (A + 1)

        l = A

        if l >= 1:
            dps_prev = 1
            dpp_prev = 1
            dpt_prev = 1

            if l == 1:
                return 3

        if l >= 2:
            dps_new = dps_prev + dpp_prev + dpt_prev
            dpp_new = dps_prev + dpt_prev # ssp, tsp, psp, stp, ptp
            dpt_new = dps_prev + dpp_prev #

            dpt_old = dpt_prev

            dps_prev = dps_new
            dpp_prev = dpp_new
            dpt_prev = dpt_new

            if l == 2:
                return dps_new + dpp_new + dpt_new

        if l >= 3:
            for i in range(3, l + 1):
                dps_new = dps_prev + dpp_prev + dpt_prev  #
                dpp_new = dps_prev + dpt_new  # ssp, tsp, psp, stp, ptp
                dpt_new = dps_prev + dpp_prev - (dpt_old * 2)

                dpt_old = dpt_prev

                dps_prev = dps_new
                dpp_prev = dpp_new
                dpt_prev = dpt_new

            ans = dps_new + dpp_new + dpt_new
        return ans % ((10 ** 9) + 7)

if __name__ == "__main__":
    A = 5
    obj = Solution()
    print(obj.solve(A))