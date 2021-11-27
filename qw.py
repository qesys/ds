import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('第一个窗口')       # 设置窗口的标题
window.geometry('200x100')     # 设置窗口的大小


content = tk.Text(window, height=3)  # 创建文本框控件，并制定文本框的高度
content.pack()

def click_button():
    """
    当按钮被点击时执行该函数
    :return:
    """
    text = content.get("0.0", "end")     # 获取全部的输入内容
    msg = "输入内容为: {text}".format(text=text)
    messagebox.showinfo(title='友情提示', message=msg)


button = tk.Button(window,
    text='发表',             # 显示在按钮上的文字
    width=15, height=2,
    command=click_button)     # 点击按钮时执行的函数
button.pack()                 # 将按钮锁定在窗口上

window.mainloop()             # 启动窗口