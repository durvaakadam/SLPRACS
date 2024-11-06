def diffie(q, alpha, XA, XB):

    YA = pow(alpha, XA, q)  # User A's public key
    YB = pow(alpha, XB, q)  
    K_A = pow(YB, XA, q)  # Shared secret key computed by User A
    K_B = pow(YA, XB, q)  # Shared secret key computed by User B
    
    if K_A != K_B:
        raise ValueError("Shared keys do not match!")

    return YA, YB, K_A

q = int(input("Enter the prime number q: "))  
alpha = int(input("Enter the generator α: "))  
XA = int(input("Enter User A's private key XA: "))  
XB = int(input("Enter User B's private key XB: ")) 

YA, YB, shared_key = diffie(q, alpha, XA, XB)

print(f"User A's public key YA: {YA}")
print(f"User B's public key YB: {YB}")
print(f"Shared key: {shared_key}")


