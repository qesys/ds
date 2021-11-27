import base64
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter import messagebox
import rsa

import md5
import _rsa

frameT = Tk()
frameT.geometry('1500x800+200+100')
frameT.title('数字签名')
frame = Frame(frameT)
frame.pack(padx=10, pady=10)  # 设置外边距
frame_1 = Frame(frameT)
frame_1.pack(padx=10, pady=10)  # 设置外边距
frame_2 = Frame(frameT)
frame_2.pack(padx=10, pady=10)  # 设置外边距
frame_3 = Frame(frameT)
frame_3.pack(padx=10, pady=10)  # 设置外边距
frame_4 = Frame(frameT)
frame_4.pack(padx=50, pady=50)  # 设置外边距
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
ent = Entry(frame, width=50, textvariable=v1).pack(fill=X, side=LEFT)  # x方向填充,靠左
ent = Entry(frame_1, width=50, textvariable=v2).pack(fill=X, side=LEFT)  # x方向填充,靠左
ent = Entry(frame_2, width=50, textvariable=v3).pack(fill=X, side=LEFT)  # x方向填充,靠左
ent = Entry(frame_3, width=50, textvariable=v4).pack(fill=X, side=LEFT)  # x方向填充,靠左
content1 = tkinter.Text(frame_4, height=12)  # 创建文本框控件，并制定文本框的高度
content1.pack()
content2 = tkinter.Text(frame_4, height=12)  # 创建文本框控件，并制定文本框的高度
content2.pack()


def RSA_create():
    # 创建密钥生成对象
    rsadata = _rsa.RSAendecrypt()
    # 生成公钥和私钥
    rsadata.generatekey()


def fileopen():
    file_sql = askopenfilename()
    if file_sql:
        v1.set(file_sql)


def md5hash():
    filepath = v1.get()
    md5hash = md5.get_md5_01(filepath)
    v2.set(md5hash)
    pass


def enmd5hash():
    hashmd5 = v2.get()
    # 加密数据
    with open(r'd:/ds/' + 'public.pem', 'r') as f:
        result = f.read()
    private = rsa.PublicKey.load_pkcs1(result)
    endata = rsa.encrypt(hashmd5.encode('utf-8'), private)
    plaintext = base64.b64encode(endata).decode('utf-8')
    v3.set(plaintext)
    files = [('Text Document', '*.txt')]
    file = asksaveasfile(mode='w', filetypes=files, defaultextension=files)
    file.write(plaintext)
    # with open(r'd:/ds/' + '签名.txt', 'w') as f:
    #     f.write(plaintext)
    pass


def demd5hash():
    file_sql = askopenfilename()
    if file_sql:
        f = open(file_sql)
        lines = f.read()
        f.close()
        # 解密数据
    with open(r'd:/ds/' + 'private.pem', 'r') as f:
        result = f.read()
    public = rsa.PrivateKey.load_pkcs1(result)
    dedata = rsa.decrypt(base64.b64decode(lines), public)
    plantext = dedata.decode('utf-8')
    v4.set(plantext)

    if v2.get() == v4.get():
        messagebox.showinfo("提示", "签名正确")
    else:messagebox.showinfo("提示","签名错误")


pass


def display_pub():
    file_sql = askopenfilename()
    if file_sql:
        f = open(file_sql)
        lines = f.readlines()
        for line in lines:
            content1.insert(END, line)
        f.close()
    pass


def display_pri():
    file_sql = askopenfilename()
    if file_sql:
        f = open(file_sql)
        lines = f.readlines()
        for line in lines:
            content2.insert(END, line)
        f.close()
    pass


btn1 = Button(frame, width=20, text='选择文件', font=("宋体", 14), command=fileopen).pack(fil=X, padx=10)
btu2 = Button(frame_1, width=20, text='数据摘要', font=("宋体", 14), command=md5hash).pack(fill=X, padx=10)
btu3 = Button(frame_2, width=20, text='签名并保存', font=("宋体", 14), command=enmd5hash).pack(fill=X, padx=10)
btu4 = Button(frame_3, width=20, text='验证签名', font=("宋体", 14), command=demd5hash).pack(fill=X, padx=10)
btu5 = Button(frame_4, width=20, text='RSA秘钥生成', font=("宋体", 14), command=RSA_create).pack(fill=X, padx=10)
btu6 = Button(frame_4, width=20, text='公钥', font=("宋体", 14), command=display_pub).pack(fill=X, padx=10)
btu7 = Button(frame_4, width=20, text='私钥', font=("宋体", 14), command=display_pri).pack(fill=X, padx=10)
frameT.mainloop()
