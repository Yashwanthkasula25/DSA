def fractional_knapsack(values, weights, capacity):
    # Create (value, weight, ratio) tuples
    items = [
        (value, weight, value / weight)
        for value, weight in zip(values, weights)
    ]

    # Sort items by ratio descending
    items = sorted(items, key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for value, weight, ratio in items:
        if remaining_capacity == 0:
            break

        take_weight = min(weight, remaining_capacity)
        total_value += value * (take_weight / weight)
        remaining_capacity -= take_weight

    return total_value

# --- User input section ---
def get_user_input():
    n = int(input("Enter number of items: "))
    
    values = []
    weights = []
    
    for i in range(n):
        v = float(input(f"Enter value of item {i+1}: "))
        w = float(input(f"Enter weight of item {i+1}: "))
        values.append(v)
        weights.append(w)
    
    capacity = float(input("Enter knapsack capacity: "))
    
    return values, weights, capacity

# --- Main execution ---
if __name__ == "__main__":
    values, weights, capacity = get_user_input()
    max_value = fractional_knapsack(values, weights, capacity)
    print(f"\nMaximum value in knapsack: {max_value:.2f}")
