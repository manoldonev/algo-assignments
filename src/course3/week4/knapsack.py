def knapsack(items, knapsack_size):
    n = len(items)

    memo = [[0 for x in range(knapsack_size + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        item_value, item_weight = items[i - 1]

        for c in range(knapsack_size + 1):
            if item_weight > c:
                memo[i][c] = memo[i - 1][c]
            else:
                memo[i][c] = max(
                    memo[i - 1][c], memo[i - 1][c - item_weight] + item_value
                )

    return memo[n][knapsack_size]


def knapsack_recursive(items, knapsack_size, n=None, memo=None):
    if n is None:
        n = len(items)

    if n == 0 or knapsack_size == 0:
        return 0

    if memo is None:
        memo = {}

    item_value, item_weight = items[n - 1]
    item_key = f"{n - 1}_{knapsack_size}"

    if item_key in memo:
        return memo[item_key]

    if item_weight > knapsack_size:
        intermediate = knapsack_recursive(items, knapsack_size, n - 1, memo)
    else:
        intermediate = max(
            knapsack_recursive(items, knapsack_size, n - 1, memo),
            knapsack_recursive(items, knapsack_size - item_weight, n - 1, memo)
            + item_value,
        )

    memo[item_key] = intermediate

    return intermediate
