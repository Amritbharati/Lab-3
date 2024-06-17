import random

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_candidate(length):
    """Generate an odd integer randomly."""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length):
    """Generate a prime number of a specified bit length."""
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    """Compute the modular inverse of a modulo m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keypair(bitsize):
    """Generate RSA key pairs of the specified bit size."""
    p = generate_prime_number(bitsize // 2)
    q = generate_prime_number(bitsize // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypt the plaintext with the given public key."""
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext with the given private key."""
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

if __name__ == "__main__":
    bitsize = int(input("Enter the bit size for RSA key generation (e.g., 1024): "))
    public_key, private_key = generate_keypair(bitsize)
    
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")
    
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_msg}")
    
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")
