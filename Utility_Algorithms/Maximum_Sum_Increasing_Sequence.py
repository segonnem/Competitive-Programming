def max_sum_increasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = arr[:]  # Copy all elements to dp, where each element is treated as a subsequence

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]

    max_sum = max(dp)
    return max_sum

#test:
arr = [1, 101, 2, 3, 100, 4, 5]
print("Maximum Sum of Increasing Subsequence is:", max_sum_increasing_subsequence(arr)) #O(n^2)
