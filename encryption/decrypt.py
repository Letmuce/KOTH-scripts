# decrypts all files (with a key)

from cryptography.fernet import Fernet
import glob
import os

# files to decrypt
directory = "/tmp/tmp.gUilhAynX1/test"

# getting the key
key = input("Enter the key: ")

# using the key
fernet = Fernet(key)

# opening directory to encrypt
for filename in glob.iglob(directory + '**/**', recursive=True):
    if not os.path.isdir(filename):
        print("decrypting " + directory)

        # opening the encrypted file
        with open(filename, 'rb') as enc_file:
            encrypted = enc_file.read()
          
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
          
        # opening the file in write mode and
        # writing the decrypted data
        with open(filename, 'wb') as dec_file:
            dec_file.write(decrypted)

print("decryption done")
