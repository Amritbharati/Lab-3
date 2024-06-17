def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient_function(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter a number to compute its Euler's Totient Function: "))
    result = euler_totient_function(n)
    print(f"Euler's Totient Function φ({n}) = {result}")
