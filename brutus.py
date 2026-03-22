from crackHTTP import brute_http_form
from crackssh import crack_ssh
from simple_hash import crack_hash
from utils import puxar_wordlist

def banner():
    print(r"""
██████╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██║   ██║██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║███████╗
██╔══██╗██╔══██╗██║   ██║   ██║   ██║   ██║╚════██║
██████╔╝██║  ██║╚██████╔╝   ██║   ╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝

        [ BRUTUS - Brute Force Framework ]
        [ Author: ANOSH | Version: 1.0 ]

--------------------------------------------------
[+] Modules Loaded:
    - Hash Cracker
    - SSH Attack
    - HTTP Form Attack
--------------------------------------------------
""")
    
if __name__ == '__main__':
    
    banner()

    op = int(input("Escolha: "))

    if op == 1:
        hash = input("HASH (md5, sha1, ...): ")
        target = input("HASH ALVO: ")
        path = input("WORDLIST: ")
        crack_hash(hash, target, path, max_threads=50)
        
    elif op == 2:
        user = input("usuário: ")
        host = input("Host: ")
        crack_ssh(host, user, "wordlist.txt")
        
    elif op == 3:
        url = input("URL: ")
        user = input("Usuário: ")
        sucesso = input("Texto de sucesso (opcional)")
        brute_http_form(url, user, "wordlist.txt", sucesso_text=sucesso)
        
    else:
        print("[*] use uma das opções acima! ")