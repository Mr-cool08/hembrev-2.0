# @hidden_cell
from windtalker import SymmetricCipher
import os
def encrypt():
    c = SymmetricCipher(password="Super secret password")
    try:
        c.encrypt_file("password.txt")
        os.remove("password.txt")
    except OSError:
        c.decrypt_file("password-encrypted.txt")
        os.remove("password-encrypted.txt")
        encrypt()
def decrypt():
    c = SymmetricCipher(password="Super secret password")
    try:
        c.decrypt_file("password-encrypted.txt")
        os.remove("password-encrypted.txt")
    except OSError:
        c.encrypt_file("password.txt")
        os.remove("password.txt")
        decrypt()
    
encrypt()
    



    
