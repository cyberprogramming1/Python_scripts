import sys  
from colorama import Fore, init 

init()

def implement_caesar_cipher(message, key, decrypt=False):
    result = ""
    
    for character in message:
        if character.isalpha():
            shift = key if not decrypt else -key
            if character.islower():
                result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += character
    return result


text_to_encrypt_or_decrypt = input(f"{Fore.GREEN}[?] Please enter your text/message: ")

choose = int(input("Encrypt text (1)/Decrypt text (2): Choose 1 or 2: "))
if choose not in [1, 2]:
    print(f"{Fore.RED}[!] Invalid choice, exiting.")
    sys.exit()

key = int(input(f"{Fore.GREEN}[?] Please specify the shift length (0-35): "))
if key < 0 or key > 35:
    print(f"{Fore.RED}[!] Your shift length should be between 0 and 35.")
    sys.exit()

if choose == 1:
    encrypted_text = implement_caesar_cipher(text_to_encrypt_or_decrypt, key)
    print(f"{Fore.YELLOW}[+] {text_to_encrypt_or_decrypt} has been encrypted as {Fore.RED}{encrypted_text}")
elif choose == 2:
    decrypted_text = implement_caesar_cipher(text_to_encrypt_or_decrypt, key, decrypt=True)
    print(f"{Fore.YELLOW}[+] {text_to_encrypt_or_decrypt} has been decrypted as {Fore.RED}{decrypted_text}")
