def rabin_karp(text, patterns):
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number
    results = {pattern: [] for pattern in patterns}
    m = max(len(pat) for pat in patterns)
    n = len(text)
    h = pow(d, m-1) % q
    p = [0] * len(patterns)
    t = 0  # Hash val 

    # compute hash val foreach
    for i, pattern in enumerate(patterns):
        for j in range(len(pattern)):
            p[i] = (d * p[i] + ord(pattern[j])) % q
        if i == 0:
            for j in range(m):
                t = (d * t + ord(text[j])) % q

    
    for i in range(n - m + 1):
        for j, pattern in enumerate(patterns):
            if p[j] == t:
                if text[i:i+len(pattern)] == pattern:
                    results[pattern].append(i)

        if i < n-m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return results

text = "abcxabcdabcdabcyabcdabcxabcd"
patterns = ["abcdabcy", "abcxabcd", "abcdabcx"]
print(rabin_karp(text, patterns)) #O(n+m)
