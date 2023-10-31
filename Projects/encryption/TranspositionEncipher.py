from Encipher import Encipher


class TranspositionEncipher(Encipher):
    def __init__(self, key):
        super().__init__(key)
        self.key = key
        self.keyLen = len(self.key)

    # 转置加密
    def encrypt(self, plaintext):
        # 变换大小写
        ciphertext = list(plaintext.swapcase())

        # 右移
        for i in range(len(ciphertext)):
            # 大写字母
            if ciphertext[i].isupper():
                ciphertext[i] = chr(65 + (ord(ciphertext[i]) + self.keyLen - 65)%26)
            # 小写字母
            elif ciphertext[i].islower():
                ciphertext[i] = chr(97 + (ord(ciphertext[i]) + self.keyLen - 97)%26)
        return ''.join(ciphertext)

    # 转置解密
    def decrypt(self, ciphertext):
        # 变换大小写
        plaintext = list(ciphertext.swapcase())

        # 右移
        for i in range(len(plaintext)):
            # 大写字母
            if plaintext[i].isupper():
                plaintext[i] = chr(65 + (ord(plaintext[i]) - self.keyLen - 65)%26)
            # 小写字母
            elif plaintext[i].islower():
                plaintext[i] = chr(97 + (ord(plaintext[i]) - self.keyLen - 97)%26)
        return ''.join(plaintext)

