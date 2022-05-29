def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (prime[p] == True):
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, limit) if prime[p]]
    return primes


def sieve_of_eratosthenes_with_bool_list(limit):
   
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 1 is not prime ;)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    # List to store prime numbers
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes, is_prime


limit = 30
primes, prime_booleans = sieve_of_eratosthenes_with_bool_list(limit)
print("Primes up to", limit, ":", primes)
print("Prime status up to", limit, ":", prime_booleans)
