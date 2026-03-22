'''
BRUTUS/
|-- WORDLIST.TXT
|-- MAIN.PY               
|-- WORDLIST_GENERATOR.PY
|-- MODULES/
        |-- HASH_CRACKER.PY
        |-- SSH_BRUTE.PY
        |-- HTTP_FROM_BRUTE.PY
|__UTILS.PY
'''
import itertools
import os


def gerar_wordlist(base_word, sufixes=None, tam_min=5, tam_max=32, output="wordlist.txt"):
    with open(output, "w", encoding="utf-8") as f:
        for word in base_word:
            f.write(word + "\n")
            for i in range(100):
                f.write(word + str(i) + "\n")
                
        chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
        for tam in range(tam_min, tam_max + 1):
            for combo in itertools.product(chars, repeat=tam):
                f.write("".join(combo) + "\n")
    '''
    BASE = ["senha", "admin", "1234567890"]
    gerar_wordlist(BASE, tam_min=5, tam_max=10)
    '''
                

def puxar_wordlist(pasta="wordlist.txt"):
    '''
    CASO VOCE TENHA A PRÓPRIA LISTA E QUEIRA PUXAR, 
    SÓ USAR ESSE DAQUI
    '''
    # caminho da pasta onde está o utils.py
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # sobe um nível se necessário (caso utils esteja em subpasta)
    #projeto_dir = os.path.dirname(base_dir)

    caminho = os.path.join(pasta)

    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo não encontrado: {caminho}")
        return []

    with open(caminho, "r", encoding="latin-1") as f:
        return [line.strip() for line in f if line.strip()]

    
