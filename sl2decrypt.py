import re

def generate_key_square(keyword):
    keyword = keyword.upper().replace('J', 'I')
    key_square = []
    seen = set()

    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            key_square.append(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen:
            key_square.append(char)

    return [key_square[i:i + 5] for i in range(0, 25, 5)]

def print_key_square(key_square):
    print("Key Square:")
    for row in key_square:
        print(" ".join(row))
    print()

def format_text(text):
    text = text.upper().replace('J', 'I')
    return re.sub(r'[^A-Z]', '', text)

def prepare_digraphs(text):
    digraphs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            digraphs.append(text[i:i + 2])
            i += 2
        else:
            digraphs.append(text[i] + 'X')
            i += 1
    return digraphs

def find_position(key_square, char):
    for r, row in enumerate(key_square):
        if char in row:
            return r, row.index(char)
    return None

def decrypt_digraph(key_square, digraph):
    row1, col1 = find_position(key_square, digraph[0])
    row2, col2 = find_position(key_square, digraph[1])
    
    if row1 == row2:
        return key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return key_square[(row1 - 1) % 5][col1] + key_square[(row2 - 1) % 5][col2]
    else:
        return key_square[row1][col2] + key_square[row2][col1]

def playfair_decrypt(text, key):
    key_square = generate_key_square(key)
    print_key_square(key_square)
    
    text = format_text(text)
    digraphs = prepare_digraphs(text)
    
    return ''.join(decrypt_digraph(key_square, digraph) for digraph in digraphs)

def main():
    keyword = input("Enter the keyword for the Playfair cipher: ").strip()
    ciphertext = input("Enter the ciphertext to decrypt: ").strip()
    
    decrypted_text = playfair_decrypt(ciphertext, keyword)
    print("\nDecrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()