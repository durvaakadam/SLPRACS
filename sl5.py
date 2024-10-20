# Function to compute gcd and the coefficients for Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to compute modular inverse of e under modulo phi_n
def mod_inverse(e, phi_n):
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % phi_n

# Function to compute n (part of both public and private keys)
def compute_n(p, q):
    return p * q

# Function to compute φ(n)
def compute_phi_n(p, q):
    return (p - 1) * (q - 1)

# Function to generate digital signature 'S'
def generate_signature(M, d, n):
    S = pow(M, d, n)
    return S

# Function to verify digital signature
def verify_signature(S, e, n):
    M_prime = pow(S, e, n)
    return M_prime

# Main program
if __name__ == "__main__":
    # Key generation
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e = int(input("Enter public key e: "))

    n = compute_n(p, q)
    phi_n = compute_phi_n(p, q)

    d = mod_inverse(e, phi_n)

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Digital signature generation
    M = int(input("\nEnter the message to sign: "))
    S = generate_signature(M, d, n)
    print(f"Digital Signature is: {S}")

    # Signature verification
    M_received = int(input("\nEnter the received message to verify: "))

    M_prime = verify_signature(S, e, n)

    if M_prime == M_received:
        print("The message is verified.")
    else:
        print("The message is altered. Discard.")
