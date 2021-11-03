from cryptography.fernet import Fernet

# Generating a key for encryption

key = Fernet.generate_key()
with open("key.key", "wb") as mykey:
    mykey.write(key)

# Encrypting part

with open("key.key", "rb") as mykey:
    key = mykey.read()

f_key = Fernet(key)
with open("text.txt", "rb") as my_text:
    text = my_text.read()
encrypted = f_key.encrypt(text)

with open("encrypted.txt", "wb") as enc_file:
    enc_file.write(encrypted)

# Decrypting part

f_key = Fernet(key)
with open("encrypted.txt", "rb") as enc_text:
    encrypted = enc_text.read()

decrypted = f_key.decrypt(encrypted)
with open("final.txt", "wb") as dec_file:
    dec_file.write(decrypted)
