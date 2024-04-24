def Z_algorithm(s):
    Z = [0] * len(s)
    l, r, K = 0, 0, 0
    for i in range(1, len(s)):
        if i > r:
            l, r = i, i
            while r < len(s) and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            K = i - l
            if Z[K] < r - i + 1:
                Z[i] = Z[K]
            else:
                l = i
                while r < len(s) and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    return Z

print(Z_algorithm("aabcaabxaaaz"))
