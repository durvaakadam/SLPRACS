def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

def modular_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def encrypt(message, e, n):
    return pow(message, e, n)

def rsa_key_generation(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modular_inverse(e, phi)
    return (n, phi, d)

# Inputs
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter the public key e: "))

n, phi, d = rsa_key_generation(p, q, e)

message = int(input("Enter the message to encrypt: "))
ciphertext = encrypt(message, e, n)

print(f"\nPublic Key (e, n): ({e}, {n})")
print(f"Private Key d: {d}")
print(f"Encrypted Message: {ciphertext}")