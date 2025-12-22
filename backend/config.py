import os

class Config:
    SECRET_KEY = "super-secret-key"
    JWT_SECRET_KEY = "jwt-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AES-256 Encryption Key
    ENCRYPTION_KEY = os.environ.get(
        "ENCRYPTION_KEY",
        "my-secret-encryption-key-1234567890123456"
    )
