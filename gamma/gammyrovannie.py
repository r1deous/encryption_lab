'''def encrypt(matrix, key):
    encrypted_matrix = []
    for row in matrix:
        encrypted_row = []
        for i, elem in enumerate(row):
            encrypted_elem = (elem + key[i % len(key)]) % 256
            encrypted_row.append(encrypted_elem)
        encrypted_matrix.append(encrypted_row)
    return encrypted_matrix

def decrypt(matrix, key):
    decrypted_matrix = []
    for row in matrix:
        decrypted_row = []
        for i, elem in enumerate(row):
            decrypted_elem = (elem - key[i % len(key)]) % 256
            decrypted_row.append(decrypted_elem)
        decrypted_matrix.append(decrypted_row)
    return decrypted_matrix

def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix

def write_matrix_to_file(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

# Чтение матрицы из файла
matrix = read_matrix_from_file('../source_texts/selection_main2.txt')
key = [1, 2, 3, 4]  # Ключ шифрования

# Шифрование
encrypted_matrix = encrypt(matrix, key)
write_matrix_to_file(encrypted_matrix, '../encrypted_texts/encrypted_gamma.txt')

# Расшифровка
decrypted_matrix = decrypt(encrypted_matrix, key)
write_matrix_to_file(decrypted_matrix, '../decrypted_texts/decrypted_gamma.txt')'''

import random

# Генерация случайного ключа
def generate_key(message_length):
    key = ''.join(random.choice('01') for _ in range(message_length))
    return key

# Функция для шифрования и расшифрования
def apply_xor_cipher(message, key):
    ciphered_message = ''.join(chr(ord(message_char) ^ int(key_char)) for message_char, key_char in zip(message, key))
    return ciphered_message

# Чтение файла с текстом
with open('../source_texts/selection_main2.txt', 'r') as file:
    text = file.read()

# Шифрование
key = generate_key(len(text))
encrypted_text = apply_xor_cipher(text, key)

# Запись зашифрованного текста в файл
with open('../encrypted_texts/encrypted_gamma.txt', 'w') as file:
    file.write(encrypted_text)

# Расшифрование
decrypted_text = apply_xor_cipher(encrypted_text, key)

# Запись расшифрованного текста в файл
with open('../decrypted_texts/decrypted_gamma.txt', 'w') as file:
    file.write(decrypted_text)