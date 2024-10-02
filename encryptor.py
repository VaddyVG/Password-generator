from cryptography.fernet import Fernet


def encrypt_password(password, key):
    '''Функция шифрования текста'''
    cipher_suite = Fernet(key)
    encrypt_password = cipher_suite.encrypt(password.encode())
    return encrypt_password


def decrypt_password(encrypted_password, key):
    '''Функция расшифровки текста'''
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password
