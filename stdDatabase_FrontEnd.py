# Developer : khom
# Date: Sunday, April 11, 2021
# Frontend

from tkinter import *
import tkinter.messagebox
import stdDatabase_BackEnd


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1450x720+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # =========================================Functions===============================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit!")
            if iExit > 0:
                root.destroy()
                return


        def clearData():
            self.txtStdID.delete(0, END)
            self.txtfname.delete(0, END)
            self.txtsname.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END)


        def addData():
            if(len(StdID.get()) != 0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),
                                              Age.get(), Gender.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(),
                                         Age.get(), Gender.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.viewData():
                studentlist.insert(END, row, str(""))


        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])

            self.txtfname.delete(0, END)
            self.txtfname.insert(END, sd[2])

            self.txtsname.delete(0, END)
            self.txtsname.insert(END, sd[3])

            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])

            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])

            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])

            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[7])

            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])


        def DeleteData():
            if (len(StdID.get()) != 0):
                stdDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()


        def searchDatabase():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),
                                              Age.get(), Gender.get(), Mobile.get()):
                studentlist.insert(END, row, str(""))


        def update():
            if (len(StdID.get()) != 0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if(len(StdID.get()) != 0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),
                                              Age.get(), Gender.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(),
                                              Age.get(), Gender.get(), Mobile.get()))


        # =========================================Frames==================================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 37, 'bold'), text="Student Database Management System",
                              bg="Ghost White", fg="red")
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1300, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=2, width=1250, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=940, height=400, padx=20, bg="Ghost White", relief=RIDGE,
                                   font=('arial', 25, 'bold'), text="Student Info\n", fg="magenta")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=460, height=200, padx=31, pady=3,
                                    bg="Ghost White", relief=RIDGE,
                                    font=('arial', 25, 'bold'), text="Student Details\n", fg="magenta")
        DataFrameRIGHT.pack(side=RIGHT)

        # ====================================Labels & Entry Widget==================================================
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="StudentID:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="First Name:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblfname.grid(row=1, column=0, sticky=W)
        self.txtfname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfname.grid(row=1, column=1)

        self.lblsname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblsname.grid(row=2, column=0, sticky=W)
        self.txtsname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtsname.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="DoB:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAddress.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=2,
                              bg="Ghost White", fg='green')
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        # ===================================ListBox & ScrollBar Widget===========================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=00, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)

        # ====================================Button Widget==================================================
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'),
                                 height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'),
                                     height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'),
                                   height=1, width=10, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'),
                                    height=1, width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'),
                                    height=1, width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'),
                                    height=1, width=10, bd=4, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'),
                              height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
