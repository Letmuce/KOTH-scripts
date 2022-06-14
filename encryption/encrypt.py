# encrypts all files in directories specified

from cryptography.fernet import Fernet
import glob
import os

#directory to recursively encrypt
directory = "/tmp/tmp.gUilhAynX1/test"

# key generation
key = Fernet.generate_key()

print(key)
 
# using the generated key
fernet = Fernet(key)

print("Encrypting files...")

# opening directory to encrypt
for filename in glob.iglob(directory + '**/**', recursive=True):
    if os.path.isdir(filename):
        print("encrypting " + filename)

    if not os.path.isdir(filename):

   # open file to encrypt 
        with open(filename, 'rb') as file:
            original = file.read()
          
    # encrypting the file
        encrypted = fernet.encrypt(original)
      
    # opening the file in write mode and writing the encrypted data
        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

print("Encryption done!")
