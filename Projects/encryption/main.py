from Encipher import Encipher
from PermutationEncipher import PermutationEncipher
from ReverseEncipher import ReverseEncipher
from TranspositionEncipher import TranspositionEncipher
from XOREncipher import XorEncipher

if __name__ == '__main__':
    key = 'tomato'
    text = "myNameIsZhang"
    # 加密器类序列
    cipherList = [TranspositionEncipher, PermutationEncipher, ReverseEncipher, XorEncipher]

    ciphertext = Encipher.encryptByEncryptList(key, text, cipherList)
    plaintext = Encipher.decryptByDecryptList(key, ciphertext, reversed(cipherList))
    print('加密后:' + ciphertext)
    print('解密后:' + plaintext)
