import argparse
import hashlib
from tqdm import tqdm
from colorama import init, Fore

# List of supported hash types
hash_names = [
    'md5', 
    'sha1', 
    'sha224', 
    'sha256', 
    'sha384', 
    'sha512',
]

def crack_hash(hash, wordlist, hash_type=None):
    
    hash_fn = getattr(hashlib, hash_type, None)
    if hash_fn is None or hash_type not in hash_names:
        raise ValueError(f'{Fore.RED}[!] Invalid hash type: {hash_type}, supported are {hash_names}')
    
    total_lines = sum(1 for line in open(wordlist, 'r'))
    print(f"{Fore.RED}[*] Cracking hash {hash} using {hash_type} with a list of {total_lines} words.")
    # open the wordlist
    with open(wordlist, 'r') as f:
        for line in tqdm(f, desc='Cracking hash', total=total_lines):
            if hash_fn(line.strip().encode()).hexdigest() == hash:
                return line

parser = argparse.ArgumentParser(description='Crack a hash using a wordlist.')
parser.add_argument('hash', help='The hash to crack.')
parser.add_argument('wordlist', help='The path to the wordlist.')
parser.add_argument('--hash-type', help='The hash type to use.', default='md5')
args = parser.parse_args()
print()
print(f"{Fore.GREEN}[+] Found password:", crack_hash(args.hash, args.wordlist, args.hash_type))


#run elemek ucun numune : 
#python.exe .\brute-force-password-cracker.py --hash-type md5 47e03bb08b9189b2365e7c8246b74b55 .\wordlist.txt 