import re
from colorama import init, Fore

init()
def check_password_strength(password):
    score = 0
    quantity = []

    if len(password) >= 8:
        score += 1
    else:
        quantity.append("Password length en azi 8 olmalidir.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        quantity.append("Password en azi bir Uppercase saxlamalidir.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        quantity.append("Password en azi bir lowercase saxlamalidir.")

    
    if re.search(r"\d", password):
        score += 1
    else:
        quantity.append("Password en azi bir eded (digit) saxlamalidir.")

    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        quantity.append("Password en azi bir nece yada bir character [!@#$%^&*(),.?\":{}|<>] saxlamalidir.")

    if  1<=score<=2:
        return f'{Fore.RED}[-] Weak password: score is: {score}'
    if 3<=score<=4:
        return f'{Fore.YELLOW}[-/+]Moderate password: score is :{score}'
    else:
        return f'{Fore.GREEN}[+] Strong password. Score is:{score}'

password = input("Input a password: ")
print(check_password_strength(password))
