
def decode_password(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_password += chr(ord(char) - 3)
    return decoded_password

def encode_pass(password):
    result = ""
    for char in password:
        if char.isdigit():
            new_digit = str(int(char) + 3)
            result += new_digit
        else:
            result += char
    return result


while True:

    print("Menu")
    print("------------")
    print("1. Encode\n2. Decode\n3. Quit\n")
    choice = (int(input("Please enter an option: ")))

    if choice == 1:
        password = (input("Please enter your password to encode: "))
        new_password = encode_pass(password)
        print("Your password has been encoded and stored!\n")

    if choice == 3:
        break
