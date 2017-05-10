import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
    chunksize = 64*1024
    basename = os.path.basename(filename)
    outputFile = os.path.dirname(filename)+"/(encrypted)"+ basename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key,AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)
            while True:
                chunk = infile.read(chunksize)

                if len(chunk)==0:
                    break
                elif len(chunk)%16 !=0:
                    chunk += b' '*(16-(len(chunk)%16))

                outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    chunksize = 64*1024
    basename = os.path.basename(filename)
    outputFile = os.path.dirname(filename)+ "/" + basename[11:]

    with open(filename, 'rb') as inFile:
        filesize = int(inFile.read(16))
        IV = inFile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = inFile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def Main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt ? :")

    if choice == 'E':
        filename = input("File to encrypt : ")
        password = input("Password: ")
        encrypt(getKey(password), filename)
        print("Done.")
    elif choice == 'D':
        filename = input("File to decrypt : ")
        password = input("Password: ")
        decrypt(getKey(password), filename)
        print("Done.")
    else:
        print("Wrong Input.")

#Main()