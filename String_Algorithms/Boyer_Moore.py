def boyer_moore(text, pattern):
    def bad_character_heuristic(pattern):
        bad_char = [-1] * 256
        for i in range(len(pattern)):
            bad_char[ord(pattern[i])] = i
        return bad_char

    m = len(pattern)
    n = len(text)
    bad_char = bad_character_heuristic(pattern)

    results = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            results.append(s)
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])

    return results

# Example usage
text = "abcxabcdabcdabcyabcdabcxabcd"
pattern = "abcdabcy"
print("Pattern found at positions:", boyer_moore(text, pattern))
