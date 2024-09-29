from pyicloud import PyiCloudService
from cryptography.fernet import Fernet

# Geração e armazenamento da chave de criptografia
key = Fernet.generate_key()
cipher = Fernet(key)

def authenticate_icloud(username, password):
    return PyiCloudService(username, password)

def upload_file(file, icloud_session):
    icloud_session.drive.upload(file)

def list_files(icloud_session):
    return icloud_session.drive.files

def encrypt_data(data):
    return cipher.encrypt(data)

def decrypt_data(data):
    return cipher.decrypt(data)
