from Encipher import Encipher
import hashlib


class XorEncipher(Encipher):
    def __init__(self, key):
        super().__init__(key)
        # 对key重新编码，避免密钥与明文相似时密文为空
        md5_machine =hashlib.md5()
        md5_machine.update(key.encode("utf-8"))
        self.key = str(md5_machine.hexdigest())

    # 将key长度扩充为text长度
    def extendKey(self, text):
        return (len(text)//len(self.key) * self.key
                + self.key[:len(text) % len(self.key)])

    def encrypt(self, plaintext):
        """
        通过密钥加密明文
        :param plaintext:
        :return: ciphertext
        """
        return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(plaintext, self.extendKey(plaintext)))

    def decrypt(self, ciphertext):
        """
        通过密钥解密密文
        :param: ciphertext
        :return: plaintext
        """
        return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(ciphertext, self.extendKey(ciphertext)))