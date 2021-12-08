from tkinter.filedialog import askopenfilename
import tkinter as tk
from PyPDF2 import PdfFileWriter, PdfFileReader

def pick_window():
    root.destroy()

    global newroot_1
    newroot_1 = tk.Tk()
    newroot_1.title("PDF Editor v1.0")
    newroot_1.geometry("500x300")

    global path
    global pages_1
    path = tk.StringVar()
    pages_1 = tk.StringVar()

    tk.Label(newroot_1, text = "目标路径:").grid(row = 0, column = 0)
    tk.Entry(newroot_1, textvariable = path).grid(row = 0, column = 1)
    tk.Button(newroot_1, text = "路径选择", command = select_path).grid(row = 0, column = 2)
    tk.Label(newroot_1, text = "要提取的页码(用英文逗号隔开写)").grid(row = 1, column = 0)
    tk.Entry(newroot_1, textvariable = pages_1).grid(row = 1, column = 1)
    tk.Button(newroot_1, text = "确定", command = pick_).grid(row = 2, column = 2)

def pick_():
    a = path.get()
    b = pages_1.get()

    newroot_1.destroy()

    b = b.split(",")
    b = list(map(int,b))

    pdf_input = PdfFileReader(open(a,"rb"))
    pdf_output = PdfFileWriter()
    page_count = pdf_input.getNumPages()
    for i in range(0,page_count):
        if((i + 1) in b):
            page_object = pdf_input.getPage(i)
            pdf_output.addPage(page_object)
    pdf_output.write(open('copy.pdf',"wb"))

def delete_window():
    root.destroy()

    global newroot_2
    newroot_2 = tk.Tk()
    newroot_2.title("PDF Editor v1.0")
    newroot_2.geometry("500x300")

    global path
    global pages_2
    path = tk.StringVar()
    pages_2 = tk.StringVar()

    tk.Label(newroot_2, text = "目标路径:").grid(row = 0, column = 0)
    tk.Entry(newroot_2, textvariable = path).grid(row = 0, column = 1)
    tk.Button(newroot_2, text = "路径选择", command = select_path).grid(row = 0, column = 2)
    tk.Label(newroot_2, text = "要删除的页码(用英文逗号隔开写)").grid(row = 1, column = 0)
    tk.Entry(newroot_2, textvariable = pages_2).grid(row = 1, column = 1)
    tk.Button(newroot_2, text = "确定", command = delete_).grid(row = 2, column = 2)

def delete_():
    a = path.get()
    b = pages_2.get()

    newroot_2.destroy()

    b = b.split(",")
    b = list(map(int,b))

    pdf_input = PdfFileReader(open(a,"rb"))
    pdf_output = PdfFileWriter()
    page_count = pdf_input.getNumPages()
    for i in range(0,page_count):
        if((i + 1) not in b):
            page_object = pdf_input.getPage(i)
            pdf_output.addPage(page_object)
    pdf_output.write(open('copy.pdf',"wb"))

def split_window():
    root.destroy()

    global newroot_3
    newroot_3 = tk.Tk()
    newroot_3.title("PDF Editor v1.0")
    newroot_3.geometry("500x300")

    global path
    global pages_3
    path = tk.StringVar()
    pages_3 = tk.StringVar()

    tk.Label(newroot_3, text = "目标路径:").grid(row = 0, column = 0)
    tk.Entry(newroot_3, textvariable = path).grid(row = 0, column = 1)
    tk.Button(newroot_3, text = "路径选择", command = select_path).grid(row = 0, column = 2)
    tk.Label(newroot_3, text = "分割点的页码").grid(row = 1, column = 0)
    tk.Entry(newroot_3, textvariable = pages_3).grid(row = 1, column = 1)
    tk.Button(newroot_3, text = "确定", command = split_).grid(row = 2, column = 2)

def split_():
    a = path.get()
    b = pages_3.get()

    newroot_3.destroy()

    b = int(b)

    pdf_input = PdfFileReader(open(a,"rb"))
    pdf_output_1 = PdfFileWriter()
    pdf_output_2 = PdfFileWriter()
    page_count = pdf_input.getNumPages()
    for i in range(0,page_count):
        if(i < b):
            page_object = pdf_input.getPage(i)
            pdf_output_1.addPage(page_object)
        if(i >= b):
            page_object = pdf_input.getPage(i)
            pdf_output_2.addPage(page_object)
    pdf_output_1.write(open('copy_1.pdf',"wb"))
    pdf_output_2.write(open('copy_2.pdf',"wb"))

def combine_window():
    root.destroy()

    global newroot_4
    newroot_4 = tk.Tk()
    newroot_4.title("PDF Editor v1.0")
    newroot_4.geometry("500x300")

    global path
    global path_1
    path = tk.StringVar()
    path_1 = tk.StringVar()

    tk.Label(newroot_4, text = "目标1路径:").grid(row = 0, column = 0)
    tk.Entry(newroot_4, textvariable = path).grid(row = 0, column = 1)
    tk.Button(newroot_4, text = "路径选择", command = select_path).grid(row = 0, column = 2)

    tk.Label(newroot_4, text = "目标2路径:").grid(row = 1, column = 0)
    tk.Entry(newroot_4, textvariable = path_1).grid(row = 1, column = 1)
    tk.Button(newroot_4, text = "路径选择", command = select_path_1).grid(row = 1, column = 2)

    tk.Button(newroot_4, text = "确定", command = combine_).grid(row = 2, column = 2)

def combine_():
    a = path.get()
    a_1 = path_1.get()

    newroot_4.destroy()

    pdf_input_1 = PdfFileReader(open(a,"rb"))
    pdf_input_2 = PdfFileReader(open(a_1,"rb"))
    pdf_output = PdfFileWriter()

    page_count_1 = pdf_input_1.getNumPages()
    page_count_2 = pdf_input_2.getNumPages()

    for i in range(0,page_count_1):
        page_object = pdf_input_1.getPage(i)
        pdf_output.addPage(page_object)
    for j in range(0,page_count_2):
        page_object = pdf_input_2.getPage(j)
        pdf_output.addPage(page_object)

    pdf_output.write(open('copy.pdf',"wb"))


def select_path():
    path_ = askopenfilename()
    path.set(path_)

def select_path_1():
    path_ = askopenfilename()
    path_1.set(path_)

root = tk.Tk()

root.title("PDF Editor v1.0")
root.geometry("270x110")


tk.Button(root, text = "提取页面", command = pick_window).grid(row = 1, column = 1, padx = 20, pady = 10)
tk.Button(root, text = "删除页面", command = delete_window).grid(row = 1, column = 2, padx = 20, pady = 10)
tk.Button(root, text = "分割PDF", command = split_window).grid(row = 2, column = 1, padx = 20, pady = 10)
tk.Button(root, text = "合并PDF", command = combine_window).grid(row = 2, column = 2, padx = 20, pady = 10)

root.mainloop()

