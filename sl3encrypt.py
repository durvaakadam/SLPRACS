def generate_key(plaintext, key):
    key_list = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_list.append(key[key_index % len(key)].upper())
            key_index += 1
        else:
            key_list.append(char)  # Preserve non-alphabet characters

    return "".join(key_list)

def print_keystream(key):
    keystream = [ord(char) - ord('A') for char in key if char.isalpha()]
    print(f"Keystream: {keystream}")

def encrypt_vigenere(plaintext, key):
    plaintext = ''.join(plaintext.split())  # Remove spaces
    ciphertext = []
    generated_key = generate_key(plaintext, key)

    print(f"Generated Key: {generated_key}")  # Print the repeating key
    print_keystream(generated_key)  # Print the keystream

    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = generated_key[i]

        if char.isupper():
            cipher_shift = (ord(char) - ord('A') + ord(key_char) - ord('A')) % 26
            ciphertext.append(chr(cipher_shift + ord('A')))
        else:
            cipher_shift = (ord(char) - ord('a') + ord(key_char) - ord('A')) % 26
            ciphertext.append(chr(cipher_shift + ord('a')))

    return "".join(ciphertext)

plaintext = input("Enter the plaintext: ").upper()
key = input("Enter the key: ").upper()
ciphertext = encrypt_vigenere(plaintext, key)
print(f"Ciphertext: {ciphertext}")
