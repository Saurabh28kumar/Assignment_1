from crypto_utils import encrypt_data, decrypt_data
from config import Config

def test_encryption_decryption():
    original = "1234-5678-9012"
    encrypted = encrypt_data(original, Config.ENCRYPTION_KEY)
    decrypted = decrypt_data(encrypted, Config.ENCRYPTION_KEY)

    assert original == decrypted
