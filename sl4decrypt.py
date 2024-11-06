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

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

def rsa_key_generation(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modular_inverse(e, phi)
    return n, d


p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter the public key e: "))

n, d = rsa_key_generation(p, q, e)

ciphertext = int(input("Enter the ciphertext to decrypt: "))
decrypted_message = decrypt(ciphertext, d, n)

print(f"\nPublic Key (e, n): ({e}, {n})")
print(f"Private Key d: {d}")
print(f"Decrypted Message is: {decrypted_message}")