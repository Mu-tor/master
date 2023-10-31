from Encipher import Encipher
import numpy as np

class PermutationEncipher(Encipher):
    def __init__(self, key):
        super().__init__(key)
        self.key = key
        self.col = len(self.key)


    # 列置换加密
    def encrypt(self, plaintext):
        # 将明文使用空格填充为长度为key的倍数的numpy数组
        plaintext = np.pad(np.array(list(plaintext)),
                           (0, self.col - len(plaintext) % self.col),
                           mode='constant', constant_values=' ')

        # 将明文转换成n行，key长度列的矩阵
        plaintextMatrix = plaintext.reshape((-1, self.col))

        # 按密钥的排序方式进行列置换
        plaintextMatrix = plaintextMatrix[:, self.getEncipherOrder()]
        return ''.join(plaintextMatrix.T.flatten())


    # 列置换解密
    def decrypt(self, ciphertext):
        # 将密文转换成key长度行，n列的矩阵
        ciphertextMatrix = np.array(list(ciphertext)).reshape((self.col, -1)).T

        # 按密钥的排序方式进行列置换
        ciphertextMatrix = ciphertextMatrix[:, self.getDecipherOrder()]
        return ''.join(ciphertextMatrix.flatten()).rstrip()

    # 获取加密序列
    def getEncipherOrder(self):
        return np.argsort(list(self.key))

    # 获取解密序列
    def getDecipherOrder(self):
        return np.argsort(np.argsort(list(self.key)))