def vigenere_encrypt(plaintext, keyword):
    def shift_char(char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    def char_to_number(char):
        return ord(char.upper()) - ord('A')

    keyword = keyword.upper()
    plaintext = plaintext.upper()
    encrypted_text = []
    keyword_length = len(keyword)
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = char_to_number(keyword[keyword_index % keyword_length])
            encrypted_text.append(shift_char(char, shift))
            keyword_index += 1
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

if __name__ == "__main__":
    plaintext = input("Enter your Plaintext: ")
    keyword = input("Enter your key: ")

    # Encryption
    encrypted = vigenere_encrypt(plaintext, keyword)
    print("Encrypted:", encrypted)
