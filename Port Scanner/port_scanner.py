import socket # qosulmaq ucun 
from colorama import init, Fore

#bezi rengler
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED

def is_port_open(host, port):
    """
    Host'da Portlarin aciq-qapali olub olmadigini yoxlamaq.
    """
    #yeni socket yaratmaq
    s = socket.socket()
    try:
        # Hosta ve onun daxilinde olan portlara qosulmaq
        s.connect((host, port))
        # timeout yaradiriq
        #s.settimeout(0.1)
    except:
        #qosula bilmeyende port bagli olarsa return False qaytarsin
        return False
    else:
        # qalan hallarda connection ugurludur ve ports aciqdir!
        return True
    
# Port adini qaytaran funksiya
def get_port_name(port):
    try:
        # Port nomresi ile port adini tapiriq
        return socket.getservbyport(port)
    except OSError:
        # Port ucun ad tapilmayanda Unknown qaytaririq
        return "Unknown"

# Host daxil edirik
host = input("Enter the host:")
#port araliqlarini daxil edirik.
port_1=int(input("First port is starting from :"))
port_2=int(input("Ports will continue till this port:"))
for port in range(port_1,port_2):
    if is_port_open(host, port):
        port_name=get_port_name(port)
        print(f"{GREEN}[+] {host}:{port} ({port_name})  is open      {RESET}",end="\n")
    else:
        print(f"{RED}[!] {host}:{port} is closed    {RESET}", end="\r")