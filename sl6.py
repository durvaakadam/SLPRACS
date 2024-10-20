def diffie_hellman_key_exchange(q, alpha, XA, XB):
    # Compute public keys
    YA = pow(alpha, XA, q)  # User A's public key
    YB = pow(alpha, XB, q)  # User B's public key

    # Compute shared secret keys
    K_A = pow(YB, XA, q)  # Shared secret key computed by User A
    K_B = pow(YA, XB, q)  # Shared secret key computed by User B

    # Ensure both shared keys are equal
    if K_A != K_B:
        raise ValueError("Shared keys do not match! There might be an error in the computations.")

    return YA, YB, K_A

# Input values
q = int(input("Enter the prime number q: "))  # Example: 23
alpha = int(input("Enter the generator α: "))  # Example: 5
XA = int(input("Enter User A's private key XA: "))  # Example: 6
XB = int(input("Enter User B's private key XB: "))  # Example: 15

# Perform Diffie-Hellman key exchange
YA, YB, shared_key = diffie_hellman_key_exchange(q, alpha, XA, XB)

# Output results
print(f"User A's public key YA: {YA}")
print(f"User B's public key YB: {YB}")
print(f"Shared key: {shared_key}")
