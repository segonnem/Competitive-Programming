def count_ways_and_show_solutions(coins, amount):
    #dynamic programming
    dp = [[] for _ in range(amount + 1)]
    dp[0] = [[]]
    
    for coin in coins:
        for x in range(coin, amount + 1):
            for way in dp[x - coin]:
                dp[x].append(way + [coin])

    num_ways = len(dp[amount])
    print(f"Total ways to make {amount} with {coins}: {num_ways}")
    for i, way in enumerate(dp[amount], 1):
        print(f"Way {i}: {way}")


coins = [1, 2, 5]
amount = 40
count_ways_and_show_solutions(coins, amount)

