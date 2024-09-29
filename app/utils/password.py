import bcrypt
import base64

SALT_ROUNDS = 10

def hash_password(plaintext_password: str) -> str:
    salt = bcrypt.gensalt(SALT_ROUNDS)
    password_hash_raw_as_bytes = bcrypt.hashpw(plaintext_password.encode('latin-1'), salt)
    password_hash_as_bytes = base64.b64encode(password_hash_raw_as_bytes)
    password_hash_as_str = password_hash_as_bytes.decode('ascii')
    return password_hash_as_str

def check_password(plaintext_password: str, password_hash_as_str: str) -> bool:
    password_hash_as_bytes = password_hash_as_str.encode('ascii')
    password_hash_raw_as_bytes = base64.b64decode(password_hash_as_bytes)
    return bcrypt.checkpw(plaintext_password.encode('latin-1'), password_hash_raw_as_bytes)
