# Fractional Knapsack Problem using Greedy Method
def fractional_knapsack(value, weight, capacity):
    n = len(value)
    ratio = []

    # Calculate value-to-weight ratio for each item
    for i in range(n):
        ratio.append(value[i] / weight[i])

    # Sort items by ratio in descending order
    items = list(zip(value, weight, ratio))
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    for v, w, r in items:
        if capacity >= w:
            # Take the whole item
            capacity -= w
            total_value += v
        else:
            # Take a fraction of the item
            fraction = capacity / w
            total_value += v * fraction
            capacity = 0
            break  # Knapsack is full
    return total_value


# Example input
values = [30, 40, 45, 77, 90]
weights = [5, 10, 15, 22, 25]
capacity = 60

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value in Knapsack =", max_value)
