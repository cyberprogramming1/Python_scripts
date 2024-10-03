import hashlib
from colorama import init, Fore
init()


def calc_hash(file_path, hash_function):
      hash_func = None
      if hash_function.lower() == 'md5':
         hash_func = hashlib.md5()
      elif hash_function.lower() == 'sha1':
         hash_func = hashlib.sha1()
      elif hash_function.lower() == 'sha256':
         hash_func = hashlib.sha256()
      else:
         raise ValueError("Invalid hash function. Use 'MD5', 'SHA-1', or 'SHA-256'.")
      
      file_path = file_path.strip('"')

      try:
        
         with open(file_path, 'rb') as f:
               while partions := f.read(4096):
                  hash_func.update(partions)
         return hash_func.hexdigest()
      except FileNotFoundError:
         return f"Error: File '{file_path}' not found."

def verify_hash(file_path, hash_function, expected_hash):
    
    calculated_hashed = calc_hash(file_path, hash_function)
    
    if isinstance(calculated_hashed, str) and "Error" in calculated_hashed:
        return calculated_hashed

    if calculated_hashed == expected_hash.lower():
        return True
    else:
        return False

 
file_path = input("Enter the path to the file: ")
hash_function = input("Enter the hash function to use (MD5, SHA-1, SHA-256): ")
expected_hash = input("Enter the expected hash value (for verification): ").lower()

    # Compute and verify the hash
result = verify_hash(file_path, hash_function, expected_hash)
    
if isinstance(result, str):
        print(result)
elif result:
         print(f"{Fore.GREEN}[+] Hash verification successful. The file is original.")
else:
      print(f"{Fore.RED}[-] Hash verification failed. This may indicate tampering or non-original software.")
      #hash ozunu gosterir
      print(f"Calculated hash: {Fore.YELLOW}{calc_hash(file_path, hash_function)}{Fore.RESET}")
