from abc import abstractmethod


class Encipher:
    def __init__(self, key):
        self.key = key

    @abstractmethod
    def encrypt(self, plaintext):
        """
        通过密钥加密明文
        :param plaintext:
        :return: ciphertext
        """
        pass

    @abstractmethod
    def decrypt(self, ciphertext):
        """
        通过密钥解密密文
        :param: ciphertext
        :return: plaintext
        """
        pass

    @staticmethod
    def getEncipherList(key, cipherList):
        # 获取加密器对象
        cipherList = [cipher(key) for cipher in cipherList]
        return cipherList

    @staticmethod
    def encryptByEncryptList(key, plaintext, encryptList):
        """
        通过加密列表对明文依次加密
        :param plaintext:
        :param encryptList:
        :return: ciphertext
        """
        # 获取加密器对象
        encryptList = Encipher.getEncipherList(key, encryptList)

        ciphertext = plaintext
        # 使用加密器依次加密
        for i in range(len(encryptList)):
            ciphertext = encryptList[i].encrypt(ciphertext)
        return ciphertext

    @staticmethod
    def decryptByDecryptList(key, ciphertext, decryptList):
        """
        通过解密列表对密文依次解密
        :param ciphertext:
        :param decryptList:
        :return: plaintext
        """
        # 获取加密器对象
        decryptList = Encipher.getEncipherList(key, decryptList)

        plaintext = ciphertext
        # 使用加密器依次解密
        for i in range(len(decryptList)):
            plaintext = decryptList[i].decrypt(plaintext)
        return plaintext