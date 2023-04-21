from Cryptodome.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()

#
with open('private.pem', 'wb') as f:
    f.write(privateKey)

with open('public.pem', 'wb') as f:
    f.write(publicKey)

print('Private key saved to private.pem')
print('Private key saved to public.pem')
print('Done')

# Gerar as Chaves Publicas e Privadas no bash do Git
# Command Line python generatePrivate_Public_KEY.py
