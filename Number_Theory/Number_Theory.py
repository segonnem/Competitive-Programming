

from math import sqrt
from fractions import Fraction


'''Integer Partition'''
def decompo_somme_generateur(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1] #(One of the fastest code ever!)


def sieve_with_smallest_prime_factor(limit):
    spf = list(range(limit + 1))  # Smallest prime factor for each number
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:  # Check if i is a prime number
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def prime_factorization(n, spf):
    factor_counts = {}
    while n != 1:
        prime_factor = spf[n]
        if prime_factor in factor_counts:
            factor_counts[prime_factor] += 1
        else:
            factor_counts[prime_factor] = 1
        n //= prime_factor
    return factor_counts


limit = 100
spf = sieve_with_smallest_prime_factor(limit)
n = 60
factors = prime_factorization(n, spf)
print("Prime factorization of", n, ":", factors)


def sieve_of_eratosthenes(limit):
    # Boolean list initialization: True means "prime"
    prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (prime[p] == True):
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    return prime




def pandigital(number):
    num_str = str(number)
    digit_set = set(num_str)  # unique digits in the number
    n = len(num_str)
    return digit_set == set(map(str, range(1, n + 1)))  # Compare with the set of '1' to 'n'

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]  # Compare string with its reverse

