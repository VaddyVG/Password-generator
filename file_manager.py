import os


def save_password(name, encrypted_password, filename="passwords_encrypted.txt"):
    '''Сохранение пароля в папке'''
    with open(filename, "a") as my_file:
        my_file.write(f"{name},{encrypted_password.decode()}\n")
    print(f"Пароль сохранен в файл {filename} в зашифрованном виде.")


def find_password_by_name(name, filename="passwords_encrypted.txt"):
    if not os.path.exists(filename):
        print("Файл с паролями не найден")
        return None
    
    with open(filename, "r") as my_file:
        for line in my_file:
            saved_name, encrypted_password = line.strip().split(",")
            if saved_name == name:
                return encrypted_password
    return None


def delete_password(name, filename="passwords_encrypted.txt"):
    '''Функция удаления пароля по имени'''
    if not os.path.exists(filename):
        print("Файл с паролями не найден")
        return False
    
    lines = []
    found = False

    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            saved_name, _ = line.strip().split(",")
            if saved_name != name:
                file.write(line)
            else:
                found = True
        
    if found:
        print(f"Пароль с именем {name} удален")
    else:
        print(f"Пароль с именем '{name}' не найден.")
    return found


def update_password(name, new_encrypted_password, filename="passwords_encrypted.txt"):
    '''Функция обновления пароля'''
    if not os.path.exists(filename):
        print("Файл с паролями не найден.")
        return False

    lines = []
    found = False
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    with open(filename, 'w') as file:
        for line in lines:
            saved_name, _ = line.strip().split(',')
            if saved_name == name:
                file.write(f"{name},{new_encrypted_password.decode()}\n")
                found = True
            else:
                file.write(line)

    if found:
        print(f"Пароль с именем '{name}' обновлен.")
    else:
        print(f"Пароль с именем '{name}' не найден.")
    return found


def list_all_passwords(filename="passwords_encrypted.txt"):
    if not os.path.exists(filename):
        print("Файл с паролями не найден.")
        return []
    
    passwords = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Проверяем, что строка не пустая
                saved_name, _ = line.strip().split(',')
                passwords.append(saved_name)

    if passwords:
        print("Сохраненные пароли:")
        for password_name in passwords:
            print(f"- {password_name}")
    else:
        print("Пароли отсутствуют.")
    
    # Добавляем паузу для просмотра результатов
    input("\nНажмите Enter для возврата в меню...")
