def vigenere_decrypt(ciphertext, keyword):
    def shift_char(char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base - shift) % 26 + base)
        return char

    def char_to_number(char):
        return ord(char.upper()) - ord('A')

    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    decrypted_text = []
    keyword_length = len(keyword)
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = char_to_number(keyword[keyword_index % keyword_length])
            decrypted_text.append(shift_char(char, shift))
            keyword_index += 1
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

if __name__ == "__main__":
    ciphertext = input("Enter your Encrypted Text: ")
    keyword = input("Enter your key: ")

    # Decryption
    decrypted = vigenere_decrypt(ciphertext, keyword)
    print("Decrypted:", decrypted)

