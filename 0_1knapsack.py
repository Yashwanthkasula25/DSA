def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# ---------- 🧾 User Input ----------
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    v = int(input(f"Enter value of item {i + 1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter the capacity of the knapsack: "))

# ---------- 🧮 Solve ----------
max_value = knapsack_01(weights, values, capacity)

# ---------- 📤 Output ----------
print(f"\nMaximum value that can be carried: {max_value}")
