import os
from cryptography.fernet import Fernet

# Get the token from the environment variable
var = os.getenv("DISCORD_TOKEN")

# Generate a key and create a Fernet instance
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Encrypt the token
msg_encriptada = fernet.encrypt(var.encode())

# Save the encrypted token to a file
with open("token_encriptado.txt", "wb") as arquivo:
    arquivo.write(msg_encriptada)

# Save the key to a separate file (do NOT commit this to GitHub)
with open("chave.key", "wb") as arq_chave:
    arq_chave.write(chave)

print("Token Encriptado Salvo")