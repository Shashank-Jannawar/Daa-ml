def knapsack(wGiven, val):
    maxW = 50
    dp = [[0 for _ in range(maxW+1)] for _ in range(len(wGiven)+1)]

    for i in range(1, len(wGiven)+1):
        for w in range(1, maxW+1):
            if wGiven[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wGiven[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[-1][-1]


w = [10, 20, 30]
val = [60, 100, 120]
print(knapsack(w, val))
