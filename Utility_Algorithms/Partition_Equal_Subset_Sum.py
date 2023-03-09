def can_partition(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False, [], []
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True 
    prev = [None] * (target + 1)
    prev[0] = []  # Initializing with an empty subset for zero sum
    
    for num in nums:
        # Traverse backwards to prevent using the same item more than once
        for i in range(target, num - 1, -1):
            if dp[i - num] and dp[i] == False: 
                dp[i] = True
                prev[i] = prev[i - num] + [num]
    
    if not dp[target]:
        return False, [], []
    
    subset1 = prev[target]
    subset2 = []
    
    item_count = {x: 0 for x in nums}
    for num in nums:
        item_count[num] += 1
    
    for num in subset1:
        item_count[num] -= 1
    
    for num in nums:
        if item_count[num] > 0:
            subset2.append(num)
            item_count[num] -= 1
    
    return True, subset1, subset2

#test
nums = [1, 5, 11, 5, 2, 3, 1, 4]
result, subset1, subset2 = can_partition(nums)
if result:
    print("Can partition:", result)
    print("Subset 1:", subset1)
    print("Subset 2:", subset2)
else:
    print("Cannot partition")


