def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.keys())

    for i in range(1, n + 1):
        item = item_list[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_list[i - 1]
            selected_items.append(item)
            w -= items[item]['cost']

    selected_items.reverse()
    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items, total_calories = greedy_algorithm(items, budget)
print("\nВибрані страви (Greedy):", selected_items)
print("Загальна кількість калорій (Greedy):", total_calories)

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nВибрані страви (DP):", selected_items_dp)
print("Загальна кількість калорій (DP):", total_calories_dp)