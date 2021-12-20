def karatsuba(x, y):
    # Base case for recursion: single digit multiplication
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1, low1 = x // 10**m, x % 10**m
    high2, low2 = y // 10**m, y % 10**m

    # Recursively calculate three products of n/2 sized numbers
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Combine the results using Karatsuba's formula:
    # x * y = (z2 * 10^(2*m)) + ((z1 - z2 - z0) * 10^m) + z0
    return z2 * 10**(2 * m) + (z1 - z2 - z0) * 10**m + z0

x = 123456789
y = 987654321
product = karatsuba(x, y)
print("Product of", x, "and", y, "is", product, x*y)
