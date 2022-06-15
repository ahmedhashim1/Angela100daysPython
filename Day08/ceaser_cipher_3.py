alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(user_text, shift_amount, direct):
    cipher_text = ""
    for letter in user_text:
        position = alphabet.index(letter)
        if direct == "encode":
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        elif direct == "decode":
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]

    print(f"The {direct}d text is {cipher_text}")


def ceaser_ang(user_text, shift_amount, direct):
    cipher_text = ""
    if direct == "decode":
        shift_amount *= -1
    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]

    print(f"The {direct}d text is {cipher_text}")

ceaser_ang(user_text=text, shift_amount=shift, direct=direction)