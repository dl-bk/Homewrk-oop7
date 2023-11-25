# Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів.

from typing import Any
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self):
        
        self.__key = Fernet.generate_key()
        self.__cipher_suite = Fernet(self.__key)

    def encryption(self, data):
        
        cipher_text = self.__cipher_suite.encrypt(data.encode())
        return cipher_text

    def decryption(self, cipher_text):
        
        plain_text = self.__cipher_suite.decrypt(cipher_text).decode()
        return plain_text


class TextModifier(EncryptionManager):
    def __init__(self, text) -> None:
        self.text = text
    
    def __str__(self) -> str:
        return self._text
    
    def __call__(self) -> Any:
        print("I have no idea what to do here")
    
    def to_upper(self):
        self._text = self.text.upper()
        return self._text
    
    def to_lower(self):
        self.text = self.text.lower()

    def space_del(self):
        self.text = self.text.replace(" ", "")
        return self.text
    
    def encryption(self):
        super().__init__()
        return super().encryption(self.text)
    
    def decryption(self, cipher_text):
        return super().decryption(cipher_text)

tm = TextModifier("ara")
encrypted = tm.encryption()
print(encrypted)

decrypted = tm.decryption(encrypted)

print(decrypted)

tm()