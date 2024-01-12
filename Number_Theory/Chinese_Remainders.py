def chinese_remainder_theorem(a, n):
    sum = 0
    prod = 1
    for ni in n:
        prod *= ni

    for ai, ni in zip(a, n):
        p = prod // ni
        sum += ai * mul_inv(p, ni) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

a = [2, 3, 1]
n = [3, 4, 5]
print("x =", chinese_remainder_theorem(a, n))