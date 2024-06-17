import random

def generate_private_key(p):
    """Generate a private key randomly."""
    return random.randint(2, p - 2)

def generate_public_key(g, private_key, p):
    """Generate a public key from a private key."""
    return pow(g, private_key, p)

def compute_shared_secret(public_key, private_key, p):
    """Compute the shared secret using a public key and a private key."""
    return pow(public_key, private_key, p)

if __name__ == "__main__":
    # Choose a large prime number p and a base g (g is a primitive root modulo p)
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a primitive root modulo p (g): "))

    # Alice generates her private and public keys
    alice_private_key = generate_private_key(p)
    alice_public_key = generate_public_key(g, alice_private_key, p)
    print(f"Alice's private key: {alice_private_key}")
    print(f"Alice's public key: {alice_public_key}")

    # Bob generates his private and public keys
    bob_private_key = generate_private_key(p)
    bob_public_key = generate_public_key(g, bob_private_key, p)
    print(f"Bob's private key: {bob_private_key}")
    print(f"Bob's public key: {bob_public_key}")

    # Both Alice and Bob compute the shared secret
    alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, p)
    bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, p)
    
    print(f"Alice's shared secret: {alice_shared_secret}")
    print(f"Bob's shared secret: {bob_shared_secret}")

    # Verify that the shared secret is the same
    if alice_shared_secret == bob_shared_secret:
        print("The shared secret is successfully exchanged!")
    else:
        print("The shared secret exchange failed.")
