import random

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def miller_rabin_test(d, n):
    a = 2 + random.randint(1, n - 4)
    x = modular_exponentiation(a, d, n)
    
    if x == 1 or x == n - 1:
        return True
    
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        
        if x == 1:
            return False
        if x == n - 1:
            return True
    
    return False

def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n - 1
    while d % 2 == 0:
        d //= 2
    
    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    
    return True

if __name__ == "__main__":
    n = int(input("Enter a number to check for primality: "))
    k = 5  # Number of iterations
    
    if is_prime(n, k):
        print(f"{n} is probably prime.")
    else:
        print(f"{n} is composite.")
