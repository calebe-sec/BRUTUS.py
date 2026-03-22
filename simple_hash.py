
from concurrent.futures import ThreadPoolExecutor
from utils import puxar_wordlist
from tqdm import tqdm
import hashlib
import threading

event = threading.Event()

def crack_hash(tipo_hash, hash_alvo, wordlist_path, max_threads=50):
    wordlist = puxar_wordlist(wordlist_path)

    hash_func = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
        }.get(tipo_hash.lower())

    if not hash_func:
        print("[*] TIPO DE HASH NÃO SUPORTADO!!")
        return None

    hash_alvo = hash_alvo.lower()

    def worker(word):
                if event.is_set():
                        return None

                tentativa = hash_func(word.encode(errors="ignore")).hexdigest()

                

                if tentativa == hash_alvo:
                        event.set()
                        return word
                return None

    resultado = None

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
                results = []

                for result in tqdm(executor.map(worker, wordlist), total=len(wordlist),desc=f"Cracking {tipo_hash}"):
                    if result:
                        resultado = result
                        break


                if resultado:
                    print(f"[+] HASH QUEBRADO! SENHA: {resultado}")
                else:
                    print("[*} HASH NÃO ENCONTRADO!")

                return resultado

def main():
        #kicking the tires
        hash = input("HASH (md5, sha1, ...): ")
        target = input("HASH ALVO: ")
        path = input("WORDLIST: ")
        crack_hash(hash, target, path, max_threads=50)
if __name__ == '__main__':
    main()
    
