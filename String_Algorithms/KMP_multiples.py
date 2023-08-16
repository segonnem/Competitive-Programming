def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP_search_single(text, pattern, lps):
    n = len(text)
    m = len(pattern)
    i = j = 0
    results = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            results.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results

def KMP_search(text, patterns):
    results = {}
    for pattern in patterns:
        lps = build_lps(pattern)
        results[pattern] = KMP_search_single(text, pattern, lps)
    return results

# Example usage
text = "abcxabcdabcdabcyabcdabcxabcd"
patterns = ["abc", "abcxabcd", "abcdabcx"]
print(KMP_search(text, patterns))

