
val = [1,2,3,4]
weight = [10,20,30,40]
memo = [[-1 for j in range(W)] for i in range(N)]
def knapsack(W, N):
    if W == 0 or N == 0:
        return 0
    if memo[W][N] != -1:
        return memo[W][N]
    if weight[N-1] <= W:
        memo[W][N] = max(knapsack(W-weight[N-1], N-1) + val[N-1], knapsack(W, N-1))
    else:
        memo[W][N] = knapsack(W, N-1)