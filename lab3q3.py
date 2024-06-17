def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient_function(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, n):
    if gcd(g, n) != 1:
        return False
    
    phi = euler_totient_function(n)
    factors = factorize(phi)
    
    for factor in factors:
        if pow(g, phi // factor, n) == 1:
            return False
    return True

def factorize(n):
    factors = set()
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors.add(p)
            n //= p
        p += 1
    if n > 1:
        factors.add(n)
    return factors

def find_primitive_roots(n):
    if n == 2:
        return [1]
    
    phi = euler_totient_function(n)
    primitive_roots = []
    for g in range(2, n):
        if is_primitive_root(g, n):
            primitive_roots.append(g)
    return primitive_roots

if __name__ == "__main__":
    n = int(input("Enter a number to find its primitive roots: "))
    roots = find_primitive_roots(n)
    if roots:
        print(f"The primitive roots of {n} are: {roots}")
    else:
        print(f"There are no primitive roots for {n}.")
