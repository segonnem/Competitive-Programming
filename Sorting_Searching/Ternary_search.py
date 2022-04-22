def ternary_search(f, left, right, absolute_precision):
    while abs(right - left) > absolute_precision:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if f(m1) < f(m2):
            right = m2
        else:
            left = m1
    return (left + right) / 2

# Example unimodal function
def f(x):
    return (x - 2) ** 2 + 3

min_point = ternary_search(f, 0, 5, 1e-5)
print("Minimum of f(x) occurs at x =", min_point)
