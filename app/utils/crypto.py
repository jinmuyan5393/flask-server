# app/utils/crypto.py
from Crypto.Cipher import AES
import base64
import json


def decrypt_data(encrypted_data, iv, session_key):
    session_key = base64.b64decode(session_key)
    encrypted_data = base64.b64decode(encrypted_data)
    iv = base64.b64decode(iv)

    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_data)

    # 去除填充
    decrypted = decrypted[:-decrypted[-1]]
    result = json.loads(decrypted.decode("utf-8"))

    return result