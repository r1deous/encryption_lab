def caesar_decipher(text, shift):
    result = ""

    for digit in text:
        if not digit.isdigit():
            result += digit
            continue

        shifted_digit = (int(digit) - shift) % 10
        result += str(shifted_digit)

    return result


with open("../decrypted_texts/cez_encrypt_text.txt", "r") as file:
    content = file.readlines()

with open("../encrypted_texts/cez_decrypt_selection.txt", "w") as output_file:
    for line in content:
        if not line.startswith("Ecnrypted:"):
            continue

        encrypted_numbers = line.strip().split(":")[1].strip().split()

        decrypted_numbers = [caesar_decipher(number, 3) for number in encrypted_numbers]

        output_file.write(f"Decrypted words: {' '.join(decrypted_numbers)}\n")
        output_file.write("\n")

print("Decrypt saved - '../encrypted_texts/cez_decrypt_selection.txt'")