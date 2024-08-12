def prime_sieve(limit):
    """
    Uses the Sieve of Eratosthenes to find all prime numbers up to a given limit.
    
    Parameters:
    limit (int): The upper limit to find primes.

    Returns:
    list: A list of prime numbers up to the limit.
    """
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    # Extract prime numbers
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

if __name__ == "__main__":
    limit = 300
    primes = prime_sieve(limit)
    print(f"Prime numbers up to {limit}:")
    print(primes)
