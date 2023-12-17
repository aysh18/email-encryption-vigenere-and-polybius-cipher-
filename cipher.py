def vigenere_encrypt(plain_text, keyword):
    keyword_repeated = (keyword * (len(plain_text) // len(keyword))) + keyword[:len(plain_text) % len(keyword)]
    encrypted_text = ""

    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = keyword_repeated[i]
        encrypted_char = chr(((ord(char) + ord(key_char) - 2 * ord('A')) % 26) + ord('A'))
        encrypted_text += encrypted_char

    return encrypted_text


def polybius_encrypt(text):
    polybius_square = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    encrypted_text = ""

    for char in text:
        if char == 'J':
            char = 'I'
        for i in range(5):
            for j in range(5):
                if polybius_square[i][j] == char:
                    encrypted_text += str(i + 1) + str(j + 1)

    return encrypted_text


def encrypt_email(plain_email, keyword):
    vigenere_output = vigenere_encrypt(plain_email, keyword)
    polybius_output = polybius_encrypt(vigenere_output)
    return polybius_output


def polybius_decrypt(text):
    polybius_square = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    decrypted_text = ""

    for i in range(0, len(text), 2):
        try:
            row = int(text[i]) - 1
            col = int(text[i + 1]) - 1
            decrypted_text += polybius_square[row][col]
        except ValueError:
            # Handle non-numeric characters (e.g., spaces)
            decrypted_text += text[i]

    return decrypted_text


def vigenere_decrypt(encrypted_text, keyword):
    keyword_repeated = (keyword * (len(encrypted_text) // len(keyword))) + keyword[:len(encrypted_text) % len(keyword)]
    decrypted_text = ""

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        key_char = keyword_repeated[i]
        decrypted_char = chr(((ord(char) - ord(key_char) + 26) % 26) + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text


def decrypt_email(encrypted_email, keyword):
    polybius_output = vigenere_decrypt(encrypted_email, keyword)
    vigenere_output = polybius_decrypt(polybius_output)
    return vigenere_output


# Example
plain_email = "HELLO, I AM AYESHA"
keyword = "KEY"

encrypted_email = encrypt_email(plain_email, keyword)
print("Encrypted Email:", encrypted_email)

decrypted_email = decrypt_email(encrypted_email, keyword)
print("Decrypted Email:", decrypted_email)
