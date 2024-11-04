"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher"""

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
from cryptography.fernet import Fernet
import rsa

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        # Your code goes here
        encrypted_message = ""
        for symbol in message:
            if symbol in SYMBOLS:
                symbol_index = SYMBOLS.index(symbol)
                encrypted_index = (symbol_index + self.key) % len(SYMBOLS)
                encrypted_message += SYMBOLS[encrypted_index]
            else:
                encrypted_message += symbol
        return encrypted_message

    def decrypt(self, message):
        # Your code goes here
        decrypted_message = ""
        for symbol in message:
            if symbol in SYMBOLS:
                symbol_index = SYMBOLS.index(symbol)
                decrypted_index = (symbol_index - self.key) % len(SYMBOLS)
                decrypted_message += SYMBOLS[decrypted_index]
            else:
                decrypted_message += symbol
        return decrypted_message


class FernetCipher:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, message):
        return self.cipher.encrypt(message.encode()).decode()

    def decrypt(self, token):
        return self.cipher.decrypt(token.encode()).decode()


class RSACipher:
    def __init__(self, public_key=None, private_key=None, key_size=512):
        # Generate new keys if not provided
        if public_key and private_key:
            self.public_key = public_key
            self.private_key = private_key
        else:
            self.public_key, self.private_key = rsa.newkeys(key_size)

    def encrypt(self, message):
        return rsa.encrypt(message.encode(), self.public_key)

    def decrypt(self, ciphertext):
        return rsa.decrypt(ciphertext, self.private_key).decode()


rsa_cipher = RSACipher()


def get_user_mode():
    while True:  # Keep asking until the user enters e or d.
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()

        if response.startswith("e"):
            return "encrypt"
        elif response.startswith("d"):
            return "decrypt"
        else:
            print("Please enter the letter 'e' or 'd'.")


def get_user_key():
    while True:  # Keep asking until the user enters a valid key.
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ")

        if not response.isdecimal():
            continue

        response = int(response)

        if 0 <= response <= max_key:
            return response


def main():
    print("Select encryption method:\n1. Caesar Cipher\n2. Fernet Cipher\n3. RSA Cipher")
    choice = input("> ").strip()
    mode = get_user_mode()  # Let the user enter if they are encrypting or decrypting

    if choice == "1":
        key = get_user_key()  # Let the user enter the key to use
        coder = CaesarCipher(key)

        # Let the user enter the message to encrypt/decrypt
        print(f"Enter the message to {mode}.")
        message = input("> ").upper()  # Caesar cipher only works on uppercase letters

        if mode == "encrypt":
            # Stores the encrypted/decrypted form of the message
            translated = coder.encrypt(message)
        else:
            translated = coder.decrypt(message)

        # Display the encrypted/decrypted string to the screen
        print(translated)

    elif choice == "2":
        key_input = input("Enter Fernet key (or press Enter to generate new): ").strip()
        if key_input:
            key = key_input.encode()
        else:
            coder = FernetCipher()
            key = coder.key
            print("Generated Fernet key: ", key.decode())

        coder = FernetCipher(key)
        message = input(f"Enter the message to {mode}: ")
        if mode == "encrypt":
            token = coder.encrypt(message)
            print("Encrypted:", token)
        else:
            print("Decrypted:", coder.decrypt(message))

    elif choice == "3":
        if mode == "encrypt":
            message = input("Enter the message to encrypt: ")
            encrypted_message = rsa_cipher.encrypt(message)
            print("Encrypted message :", encrypted_message)
        else:
            encrypted_message = input("Enter the RSA encrypted message to decrypt: ")
            encrypted_message = eval(encrypted_message)
            decrypted_message = rsa_cipher.decrypt(encrypted_message)
            print("Decrypted message:", decrypted_message)

    else:
        print("Invalid. Please select 1, 2, or 3.")


if __name__ == "__main__":
    while True:
        main()

        print("\n\nDo you want to run cipher one more time? Y or N")
        repeat = input("> ").lower()

        if repeat != "y":
            print("Thank you for using  Cipher.")
            break
