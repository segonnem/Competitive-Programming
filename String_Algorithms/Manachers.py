def manachers_algorithm(s):
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n
    center = right = 0
    
    for i in range(1, n-1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])  

        # Attempt to expand palindrome centered at i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        
        if i + p[i] > right:
            center, right = i, i + p[i]

    # Find the maximum element in p
    max_len, center_index = max((n, i) for i, n in enumerate(p))
    start = (center_index - max_len) // 2  
    return s[start: start + max_len]

input_string = "abcbabcbabcba"
print("Longest palindromic substring:", manachers_algorithm(input_string)) #Perform in O(n) !! bettern than dynamic approach n**2 or naive n**3
