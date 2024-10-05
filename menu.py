import subprocess
import sys
import os
import pyfiglet
from colorama import init, Fore
init()

def run_script(script_name, *args):
    try:
        # Using sys.executable to ensure the correct Python interpreter is used
        subprocess.run([sys.executable, script_name] + list(args))
    except Exception as e:
        print(f"Error running {script_name}: {e}")

def show_figlet_design():
    figlet_text = pyfiglet.figlet_format("TORPEDO")
    print(Fore.BLUE + figlet_text + Fore.RESET)

while True:
    def menu():
        show_figlet_design()
        print("Choose a script to run:")
        print("1. Brute-Force Password Cracker:")
        print("2. File Integrity Checker:")
        print("3. Password Strength Checker:")
        print("4. Port Scanner:")
        print("5. Caesar Cipher Encryption/Decryption:")
        print("6. Exit:")
        choice = input("Enter the number (1-6): ")

        if choice == '1':
            hash_value = input("Enter the hash to crack: ")
            wordlist_path = input("Enter the path to the wordlist: ")
            hash_type = input("Enter the hash type (default: md5): ") or "md5"
            run_script(r'C:\scripts\Brute-force Password Cracker\brute-force-password-cracker.py', hash_value, wordlist_path, '--hash-type', hash_type)
        elif choice == '2':
            run_script(r'C:\scripts\File Integrity Checker\file_integrity_checker.py')
        elif choice == '3':
            run_script(r'C:\scripts\Password Strength Checker\checker.py')
        elif choice == '4':
            run_script(r'C:\scripts\Port Scanner\port_scanner.py')
        elif choice == '5':
            run_script(r'C:\scripts\Simple Caesar Cipher Encoder\Decoder\smp_caesarcipher_encode_decode.py')
        elif choice == '6':
            sys.exit()
        else:
            print("Invalid choice, please enter a number between 1 and 6")

    if __name__ == "__main__":
        menu()