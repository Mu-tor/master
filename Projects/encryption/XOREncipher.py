from Encipher import Encipher


class XorEncipher(Encipher):
    def __init__(self, key):
        super().__init__(key)
        self.key = key

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