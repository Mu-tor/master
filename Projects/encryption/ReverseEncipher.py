from Encipher import Encipher

class ReverseEncipher(Encipher):
    def __init__(self, key):
        super().__init__(key)
        self.key = key

    # 反转加密
    def encrypt(self, plaintext):
        return plaintext[::-1]

    # 反转解密
    def decrypt(self, ciphertext):
        return ciphertext[::-1]