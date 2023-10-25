

def encode_password(password):
    encoded_password = ""
    for char in password:
        encoded_password += chr(ord(char) + 3)
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_password += chr(ord(char) - 3)
    return decoded_password

while True:
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = input("\nPlease enter an option: ")

    if choice == '1':
        user_input = input("Please enter your password to encode: ")
        encode_result = encode_password(user_input)
        print("Your password has been encoded and stored!")

    elif choice == '2':
        if 'encode_result' in locals() and 'user_input' in locals():
            print(f"The encoded password is {encode_result}, and the original password is {user_input}")
        else:
            print("You need to encode a password first!")

    elif choice == '3':
        break
