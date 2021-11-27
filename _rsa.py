import base64
from tkinter.filedialog import asksaveasfile

import rsa


class RSAendecrypt(object):
    """
    generate public and private key (生成公钥和私钥)
    encrypt passwd (加密数据)
    decrypt passwd (解密数据)
    """

    def __init__(self, filepath=None):
        """init filepath 获取公钥或私钥存储路径"""
        if filepath is None:
            filepath = r'd:/ds/'
        self.filepath = filepath

    def generatekey(self):
        """public and private keys 生成公钥和私钥到指定的路径"""
        public, private = rsa.newkeys(1024)
        public_key = public.save_pkcs1().decode()
        private_key = private.save_pkcs1().decode()
        files = [('Text Document', '*.pem')]
        file = asksaveasfile(mode='w', filetypes=files, defaultextension=files)
        file.write(public_key)
        file2 = asksaveasfile(mode='w', filetypes=files, defaultextension=files)
        file2.write(private_key)
        # with open(self.filepath + 'private.pem', 'w') as f:
        #     f.write(private_key)
        # with open(self.filepath + 'public.pem', 'w') as f:
        #     f.write(public_key)

    def encrypt(self, enstr):
        """encrypt string 加密数据 返回加密后的值"""
        with open(self.filepath + 'public.pem', 'r') as f:
            result = f.read()
        # 解析公钥赋值
        public = rsa.PublicKey.load_pkcs1(result)
        endata = rsa.encrypt(enstr.encode('utf-8'), public)
        return base64.b64encode(endata).decode('utf-8')

    def decrypt(self, destr):
        """decrypt string 解密数据 返回被加密的值"""
        with open(self.filepath + 'private.pem', 'r') as f:
            result = f.read()
        # 解析私钥赋值
        private = rsa.PrivateKey.load_pkcs1(result)
        dedata = rsa.decrypt(base64.b64decode(destr), private)
        return dedata.decode('utf-8')


# if __name__ == '__main__':
#     # 定义一个字符串
#     jiamishuju = 'my name is gim'
#     # 创建密钥生成对象
#     rsadate = RSAendecrypt()
#     # 生成公钥和私钥
#     rsadate.generatekey()
#     # 加密数据
#     desdate = rsadate.encrypt(jiamishuju)
#     print(desdate)
#     # 解密数据
#     redate = rsadate.decrypt(desdate)
#     print(redate)

