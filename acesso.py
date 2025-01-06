import os
from cryptography.fernet import Fernet

# Caminho do Arquivo
PATH_TOKEN_ENCRIPTADO = "token_encriptado.txt"
PATH_CHAVE = "chave.key"

def valida_arquivo():
    """
    Valida se o token encriptado e a chave existem.
    Gera o FileNotFoundError se algum dos arquivos não existirem.
    """
    if not os.path.exists(PATH_TOKEN_ENCRIPTADO):
        raise FileNotFoundError(f"Arquivo não está presente: {PATH_TOKEN_ENCRIPTADO}")
    if not os.path.exists(PATH_CHAVE):
        raise FileNotFoundError(f"Arquivo não está presente: {PATH_CHAVE}")
    

def carrega_chave():
    """
    Carrega a chave de encriptação do arquivo chave.
    Retorna a chave em bytes.
    """
    valida_arquivo()
    with open(PATH_CHAVE, "rb") as arquivo_chave:
        return arquivo_chave.read()

def carrega_token_encriptado():
    """
    Carrega o token encriptado do arquivo.
    Retorna o token encriptado como bytes.
    """
    valida_arquivo()
    with open(PATH_TOKEN_ENCRIPTADO, "rb") as arquivo_token:
        return arquivo_token.read()

def decryptar_token():
    """
    Decripta o token usando a chave armazenada.
    Returna o token decriptado como string
    """
    chave = carrega_chave()
    token_encriptado = carrega_token_encriptado()
    fernet = Fernet(chave)
    try:
        return fernet.decrypt(token_encriptado).decode()
    except Exception as e:
        raise ValueError("Falha ao descriptar token. Garanta que a chave pertence ao token.") from e