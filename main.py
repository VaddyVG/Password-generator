from gen_password import generate_password
from encryptor import encrypt_password, decrypt_password
from file_manager import save_password, find_password_by_name, delete_password, update_password, list_all_passwords
from key_manager import load_key

# Загружаем ключ шифрования
key = load_key()

while True:
    print("\nМеню:")
    print("1. Сгенерировать новый пароль")
    print("2. Найти пароль по имени")
    print("3. Удалить пароль")
    print("4. Обновить пароль")
    print("5. Показать все сохраненные пароли")
    print("6. Выйти")

    choice = input("\nВыберите действие (1-6): ")

    if choice == "1":
        # Генерация пароля
        length = int(input("Введите длину пароля: "))
        use_uppercase = input("Использовать ли буквы верхнего регистра? (y/n): ").lower() == 'y'
        use_digits = input("Использовать ли цифры? (y/n): ").lower() == 'y'
        use_special = input("Использовать ли специальные символы? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_special)
        print("Ваш сгенерированный пароль:", password)

        # Шифрование пароля
        encrypted_password = encrypt_password(password, key)

        # Сохранение пароля
        password_name = input("Введите имя для пароля (например, 'Электронная почта'): ")
        save_password(password_name, encrypted_password)

    elif choice == "2":
        # Поиск пароля
        search_name = input("Введите имя для поиска пароля: ")
        found_encrypted_password = find_password_by_name(search_name)
        if found_encrypted_password:
            decrypted_password = decrypt_password(found_encrypted_password.encode(), key)
            print(f"Найденный пароль для {search_name}: {decrypted_password}")
            break
        else:
            print("Пароль не найден")

    elif choice == "3":
        # Удаление пароля
        delete_name = input("Введите имя для удаления пароля: ")
        delete_password(delete_name)
        break

    elif choice == "4":
        # Обновление пароля
        update_name = ("Введите имя для обновления пароля: ")
        found_encrypted_password = find_password_by_name(update_name)

        if found_encrypted_password:
            # Генерация нового пароля
            length = int(input("Введите длину нового пароля: "))
            use_uppercase = input("Использовать ли буквы верхнего регистра? (y/n): ").lower() == 'y'
            use_digits = input("Использовать ли цифры? (y/n): ").lower() == 'y'
            use_special = input("Использовать ли специальные символы? (y/n): ").lower() == 'y'

            new_password = generate_password(length, use_uppercase, use_digits, use_special)
            new_encrypted_password = encrypt_password(new_password, key)
            update_password(update_name, new_encrypted_password)
        else:
            print("Пароль не найден для обновления.")

    elif choice == "5":
        # Показать все пароли
        list_all_passwords()

    elif choice == "6":
        print("Выход из программы")
        break

    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
