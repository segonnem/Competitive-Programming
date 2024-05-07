def longest_increasing_subsequence(a):

    n = len(a)
    if n == 0:
        return 0, []
    
    dp = [1] * n
    predecessor = [-1] * n
    end = [0] * (n + 1)
    length_LIS = 0  # Length of longest increasing subsequence found

    for i in range(n):
        # Binary search for the largest positive j ≤ L such that a[end[j]] < a[i]
        l = 1
        r = length_LIS
        while l <= r:
            mid = (l + r) // 2
            if a[end[mid]] < a[i]:
                l = mid + 1
            else:
                r = mid - 1
        
        pos = l
        dp[i] = pos
        predecessor[i] = end[pos - 1]
        

        if pos > length_LIS:
            length_LIS = pos
            end[pos] = i
        elif a[i] < a[end[pos]]:
            end[pos] = i

    lis = [0] * length_LIS
    k = end[length_LIS]
    for j in range(length_LIS - 1, -1, -1):
        lis[j] = a[k]
        k = predecessor[k]

    return length_LIS, lis


#test
N,subseq = longest_increasing_subsequence([1,99,100,2,3,4,99,100,2,6,9,10])
print(N,subseq)


#Note L --> (-1)*L for decreasing sequence
