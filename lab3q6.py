import random

def mod_exp(base, exp, mod):
    """Compute (base^exp) % mod using modular exponentiation."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def generate_prime(bitsize):
    """Generate a large prime number."""
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    while True:
        p = random.randrange(2**(bitsize-1), 2**bitsize)
        if is_prime(p):
            return p

def find_primitive_root(p):
    """Find a primitive root modulo p."""
    def is_primitive_root(g, p):
        seen = set()
        for i in range(1, p):
            val = mod_exp(g, i, p)
            if val in seen:
                return False
            seen.add(val)
        return True

    # Check for small values first
    if p == 2:
        return 1
    if p == 3:
        return 2

    # Find the smallest primitive root
    g = 2
    while not is_primitive_root(g, p):
        g += 1
    return g

def generate_keypair(p):
    """Generate public and private keys for ElGamal."""
    # Select a random private key
    x = random.randint(2, p - 2)
    
    # Calculate corresponding public key
    g = find_primitive_root(p)
    y = mod_exp(g, x, p)
    
    return (p, g, y), x

def encrypt(message, public_key):
    """Encrypt a message using ElGamal."""
    p, g, y = public_key
    k = random.randint(2, p - 2)
    r = mod_exp(g, k, p)
    s = (message * mod_exp(y, k, p)) % p
    return r, s

def decrypt(ciphertext, private_key, public_key):
    """Decrypt a ciphertext using ElGamal."""
    p, g, y = public_key
    r, s = ciphertext
    x = private_key
    inverse_y = mod_exp(y, p - 1 - x, p)
    message = (s * inverse_y) % p
    return message

if __name__ == "__main__":
    bitsize = int(input("Enter the bit size for prime generation (e.g., 256): "))
    
    # Generate a large prime number p
    p = generate_prime(bitsize)
    print(f"Selected prime p: {p}")
    
    # Generate key pairs
    public_key, private_key = generate_keypair(p)
    print(f"Public key (p, g, y): {public_key}")
    print(f"Private key x: {private_key}")
    
    # Encrypt a message
    message = int(input("Enter a message to encrypt (as an integer): "))
    ciphertext = encrypt(message, public_key)
    print(f"Encrypted ciphertext (r, s): {ciphertext}")
    
    # Decrypt the ciphertext
    decrypted_message = decrypt(ciphertext, private_key, public_key)
    print(f"Decrypted message: {decrypted_message}")
