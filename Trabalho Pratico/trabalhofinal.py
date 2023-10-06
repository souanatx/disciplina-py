# Trabalho Prático de Ana Teixeira

import random
import string

def is_valid_name(name):
    return name.isalpha()

def get_yes_or_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 's' or user_input == 'n':
            return user_input
        else:
            print("Erro, input inaceitável. Tente novamente.")

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols):
    character_set = ""
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        return "Nenhum conjunto de caracteres selecionado."

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def check_password_strength(password):
    checks = [
        len(password) >= 8,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char in string.punctuation for char in password)
    ]

    if all(checks):
        return "Senha forte"
    elif all(checks[:-1]):
        return "Senha média"
    else:
        return "Senha fraca"

def transform_char(char, shift):
    if char.islower():
        return chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    elif char.isupper():
        return chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    else:
        return char

def encrypt_message(plain_text):
    return ''.join(transform_char(char, 1) for char in plain_text)

def decrypt_message(encrypted_text):
    return ''.join(transform_char(char, -1) for char in encrypted_text)

def print_intro():
    intro = """
*****************************************************
*                                                   *
*        \033[32mTrabalho Prático de Ana Teixeira\033[0m           *
*                                                   *
*****************************************************
    """
    print(intro)

def main():
    print_intro()
    while True:
        user_name = input("Por favor, insira seu nome: ")
        if is_valid_name(user_name):
            break
        else:
            print("Nome inválido. Use apenas letras.")

    while True:
        print("\nMenu:")
        print("1. Gerar Password")
        print("2. Verificar Password")
        print("3. Criptografar mensagem")
        print("4. Decodificar mensagem")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            while True:
                try:
                    length = int(input(f"{user_name}, digite o número de caracteres da password: "))
                    break
                except ValueError:
                    print("Erro, insira um número válido.")
            use_lowercase = get_yes_or_no_input("Incluir letras minúsculas? (S/N): ") == "s"
            use_uppercase = get_yes_or_no_input("Incluir letras maiúsculas? (S/N): ") == "s"
            use_numbers = get_yes_or_no_input("Incluir números? (S/N): ") == "s"
            use_symbols = get_yes_or_no_input("Incluir símbolos? (S/N): ") == "s"

            password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)
            print(f"Password gerada: {password}")
            print("-" * 80)
        elif choice == "2":
            password = input(f"{user_name}, digite a senha a ser verificada: ")
            strength = check_password_strength(password)
            print(f"Força da senha: {strength}")
            print("-" * 80)
        elif choice == "3":
            message = input(f"{user_name}, digite a mensagem a ser criptografada: ")
            encrypted_message = encrypt_message(message)
            print(f"Mensagem criptografada: {encrypted_message}")
            print("-" * 80)
        elif choice == "4":
            encrypted_message = input(f"{user_name}, digite a mensagem criptografada a ser decodificada: ")
            decrypted_message = decrypt_message(encrypted_message)
            print(f"Mensagem decodificada: {decrypted_message}")
            print("-" * 80)
        elif choice == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")
            print("-" * 80)

if __name__ == "__main__":
    main()
