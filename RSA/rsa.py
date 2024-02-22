from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Генерация ключей
key = RSA.generate(2048)
private_key = key.exportKey()
public_key = key.publickey().exportKey()

# Шифрование
def encrypt_message(message, public_key):
    key = RSA.importKey(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return binascii.hexlify(encrypted_message)

# Расшифрование
def decrypt_message(encrypted_message, private_key):
    key = RSA.importKey(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(binascii.unhexlify(encrypted_message))
    return decrypted_message.decode()

# Чтение файла с текстом
with open('input.txt', 'r') as file:
    text = file.read()

# Шифрование
encrypted_text = encrypt_message(text, public_key)

# Запись зашифрованного текста в файл
with open('encrypted.txt', 'wb') as file:
    file.write(encrypted_text)

# Расшифрование
decrypted_text = decrypt_message(encrypted_text, private_key)

# Запись расшифрованного текста в файл
with open('decrypted.txt', 'w') as file:
    file.write(decrypted_text)