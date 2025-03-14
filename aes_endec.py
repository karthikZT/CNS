pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC)  
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size)) 
    return cipher.iv + encrypted_data

def aes_decrypt(key, encrypted_data):
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode()

data = "hello, this is how aes works"
key = get_random_bytes(16)
encrypted = aes_encrypt(key, data)
print(f"Encrypted data (in bytes): {encrypted}")

decrypted = aes_decrypt(key, encrypted)
print(f"Decrypted data: {decrypted}")
