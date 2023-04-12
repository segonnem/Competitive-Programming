import random

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    # Write (n - 1) as 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    
    def trial_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if trial_composite(a):
            return False
    return True

#test prime
n = 101
k = 5
print("Is", n, "a prime?", miller_rabin(n, k))
