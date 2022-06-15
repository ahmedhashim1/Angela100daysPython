from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def ceaser(user_text, shift_amount, direct):
    cipher_text = ""
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direct == "encode":
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
            elif direct == "decode":
                new_position = position - shift_amount
                cipher_text += alphabet[new_position]
        else:
            cipher_text += char

    print(f"The {direct}d text is {cipher_text}")

def ceaser_ang(user_text, shift_amount, direct):
    cipher_text = ""
    if direct == "decode":
        shift_amount *= -1
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char

    print(f"The {direct}d text is {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    ceaser_ang(user_text=text, shift_amount=shift, direct=direction)
    result = input("Type Yes to continue or No to exit: ").lower()

    if result == "no":
        should_continue = False
        print("Good bye!")
