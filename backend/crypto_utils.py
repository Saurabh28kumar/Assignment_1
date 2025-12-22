from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(secret):
    return base64.urlsafe_b64encode(
        hashlib.sha256(secret.encode()).digest()
    )

def encrypt_data(data, secret):
    key = generate_key(secret)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token, secret):
    key = generate_key(secret)
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()
