from tkinter import *
from tkinter import messagebox
import csv
class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        #创建姓名框
        self.name=Label(self,text="姓名")
        self.name.grid(row=0,column=0)
        v1=StringVar()
        self.name_entry=Entry(self,textvariable=v1)#绑定组件
        self.name_entry.grid(row=0, column=1,pady=15,padx=10)

        #创建学院框
        self.xueyuan = Label(self, text="学院")
        self.xueyuan.grid(row=1, column=0)
        v2 = StringVar()  # StringVar IntVar
        self.xueyuan_entry = Entry(self, textvariable=v2)
        self.xueyuan_entry.grid(row=1, column=1,pady=15)

        # 创建班级框
        self.student_class = Label(self, text="班级")
        self.student_class.grid(row=2, column=0)
        v3 = StringVar()  # StringVar IntVar
        self.student_class_entry = Entry(self, textvariable=v3)
        self.student_class_entry.grid(row=2, column=1,pady=15)

        # 创建学号框
        self.number = Label(self, text="学号")
        self.number.grid(row=3, column=0)
        v4 = StringVar()  # StringVar IntVar
        self.number_entry = Entry(self, textvariable=v4)
        self.number_entry.grid(row=3, column=1,pady=15)
        #按钮
        self.button1=Button(self,text="确认签到",command=self.sign)
        self.button1.grid(row=1, column=2,sticky=W,padx=10,pady=15)
        self.button2 = Button(self, text="退出系统", command=self.quit_system)
        self.button2.grid(row = 2, column=2,sticky=E,padx=10, pady=15)
    def sign(self):
        student_name=self.name_entry.get()
        collage=self.xueyuan_entry.get()
        classji=self.student_class_entry.get()
        num=self.number_entry.get()
        if len(student_name)==0 or len(collage)==0 or len(classji)==0 or len(num)==0:
            messagebox.showinfo("提示信息：","信息未填写完整！")
        elif len(num)!=10:
            messagebox.showinfo("提示信息")