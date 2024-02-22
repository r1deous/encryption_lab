def caesar_cipher(text, shift):
    result = ""

    for digit in text:
        if not digit.isdigit():
            result += digit
            continue

        shifted_digit = (int(digit) + shift) % 10
        result += str(shifted_digit)

    return result


with open("../source_texts/selection_text.txt", "r") as file:
    content = file.readlines()

with open("../decrypted_texts/cez_encrypt_text.txt", "w") as output_file: #зашифрованный текст
    for line in content:
        if not line or "\t" not in line:
            continue

        columns = line.strip().split("\t")

        if len(columns) < 3:
            continue

        letter = columns[1]
        numbers = columns[2].split()

        encrypted_numbers = [caesar_cipher(number, 3) for number in numbers]

        output_file.write(f"Class: {letter}\n")
        output_file.write(f"Ecnrypted: {' '.join(encrypted_numbers)}\n")
        output_file.write("\n")

print("The text has been successfully encrypted (../decrypted_texts/cez_encrypr_text.txt)")