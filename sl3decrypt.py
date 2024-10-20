def generate_key(ciphertext, key):
    key_list = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_list.append(key[key_index % len(key)].upper())
            key_index += 1
        else:
            key_list.append(char)  # Preserve non-alphabet characters

    return "".join(key_list)

def print_keystream(key):
    keystream = [ord(char) - ord('A') for char in key if char.isalpha()]
    print(f"Keystream: {keystream}")

def decrypt_vigenere(ciphertext, key):
    decryptedtext = []
    generated_key = generate_key(ciphertext, key)

    print(f"Generated Key: {generated_key}")  
    print_keystream(generated_key)  

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = generated_key[i]

        if char.isupper():
            plain_shift = (ord(char) - ord('A') - (ord(key_char) - ord('A')) + 26) % 26
            decryptedtext.append(chr(plain_shift + ord('A')))
        else:
            plain_shift = (ord(char) - ord('a') - (ord(key_char) - ord('A')) + 26) % 26
            decryptedtext.append(chr(plain_shift + ord('a')))

    return "".join(decryptedtext)

ciphertext = input("Enter the ciphertext: ").upper()
key = input("Enter the key: ").upper()
decrypted_text = decrypt_vigenere(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
