
val = [1,2,3,4]
weight = [10,20,30,40]
def knapsack(W, N):
    if W == 0 or N == 0:
        return 0
    if weight[N-1] <= W:
        return max(knapsack(W-weight[N-1], N-1) + val[N-1], knapsack(W, N-1))
    else:
        return knapsack(W, N-1)