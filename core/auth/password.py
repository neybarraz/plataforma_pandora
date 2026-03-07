# core/auth/password.py

from passlib.hash import pbkdf2_sha256


def hash_password(password: str) -> str:
    if password is None:
        password = ""
    # PBKDF2 não tem a limitação de 72 bytes do bcrypt
    return pbkdf2_sha256.hash(password)


def verify_password(password: str, hash_value: str) -> bool:
    if password is None:
        password = ""
    return pbkdf2_sha256.verify(password, hash_value)