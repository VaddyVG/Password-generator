# Генератор и шифровальщик паролей

Этот проект представляет собой простое приложение на Python для генерации, шифрования, хранения и управления паролями. Программа позволяет пользователю создавать безопасные пароли, сохранять их в зашифрованном виде, а также управлять сохраненными паролями: искать, обновлять и удалять их.

## Функциональность

- Генерация случайных паролей с учетом заданной длины и опционального использования символов верхнего регистра, цифр и специальных символов.
- Шифрование паролей с использованием библиотеки `cryptography`.
- Сохранение зашифрованных паролей в текстовом файле.
- Поиск пароля по имени.
- Удаление пароля по имени.
- Обновление пароля.
- Просмотр всех сохраненных паролей.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/VaddyVG/Password-generator.git
cd password_generator
```

2. Создайте виртульное окружение:
```bash
python3 -m venv venv
source venv/bin/activate # На Windows используйте: venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

1. Запустите программу:
```bash
python main.py
```

2. Следуйте инструкциям на экране для генерации, сохранения и управления паролями.

