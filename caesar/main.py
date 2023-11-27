from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    arr = list(text)
    encrypted_message = []
    for letter in arr:
        i = alphabet.index(letter)
        encrypted_message.append(alphabet[i + shift])
    s = ''.join(encrypted_message)
    return s

def decrypt(text, shift):
    """
    A function that takes a text input in the form of a string and a shift value that will shift each char in the string by the shift amount
    """
    arr = list(text)
    decrypted_message = []
    for letter in arr:
        i = alphabet.index(letter)
        decrypted_message.append(alphabet[i-shift])
    s = ''.join(decrypted_message)
    return s

def main():
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('Invalid Input: Try again')
        main()
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > len(alphabet):
            shift = shift % len(alphabet)
        if direction == 'encode':
            print(encrypt(text, shift))
        elif direction == 'decode':
            print(decrypt(text, shift))
main()