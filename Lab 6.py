
def decode_password(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_password += chr(ord(char) - 3)
    return decoded_password
