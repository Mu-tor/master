from Encipher import Encipher
from PermutationEncipher import PermutationEncipher
from ReverseEncipher import ReverseEncipher
from TranspositionEncipher import TranspositionEncipher
from XOREncipher import XorEncipher
import psutil
import os
import time


if __name__ == '__main__':
    # key = "zhang"
    # text = "MyNameIsZhang"
    # cip = "103232120123012302132103213112121"
    # # 加密器类序列
    # cipherList = [TranspositionEncipher, PermutationEncipher, ReverseEncipher, XorEncipher]
    # # 将输入转为加密序列
    # ciphers = [cipherList[int(i) % 4] for i in cip]
    # ciphertext = Encipher.encryptByEncryptList(key, text, ciphers)
    # print('加密后:' + ciphertext)
    # plaintext = Encipher.decryptByDecryptList(key, ciphertext, reversed(ciphers))
    # print('解密后:' + plaintext.strip())
    cipherList = [TranspositionEncipher, PermutationEncipher, ReverseEncipher, XorEncipher]
    print('---------加密系统---------')
    active = True
    while active:
        select = input('请选择要进行的操作(1.加密 2.解密 3.退出)：')
        if select == '1':
            print('0.替换 1.列置换 2.反转 3.异或')
            cip = input('请选择要进行的加密序列(如：0123)：')
            # 将输入转为加密序列
            ciphers = [cipherList[int(i) % 4] for i in cip]
            key = input("请输入密钥：")
            text = input("请输入明文：")
            start = time.process_time()
            ciphertext = Encipher.encryptByEncryptList(key, text, ciphers)
            end = time.process_time()
            print("密文：" + ciphertext)
            print(u'加密内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
            print(f'耗时：{(end - start)*1000}ms')
            print('------------------------')
        if select == '2':
            print('0.替换 1.列置换 2.反转 3.异或')
            cip = input('请输入加密序列(如：0123)：')
            # 将输入转为加密序列
            deciphers = [cipherList[int(i) % 4] for i in cip]
            key = input("请输入密钥：")
            text = input("请输入密文：")
            start = time.process_time()
            plaintext = Encipher.decryptByDecryptList(key, text, reversed(deciphers))
            end = time.process_time()
            print("明文：" + plaintext)
            print(u'解密内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
            print(f'耗时：{(end - start)*1000}ms')
            print('------------------------')
        if select == '3':
            break
