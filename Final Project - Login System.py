import tkinter.messagebox
from tkinter import *
import os
import webbrowser
window = Tk()
window.title("Login")
window.geometry("400x250")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')


def login():
    global userbox
    global passbox
    global passerror
    global usererror

    cred_user = userbox.get()
    cred_pass = passbox.get()

    listfile = os.listdir()
    if cred_user in listfile:
        file1 = open(cred_user, "r")
        verify = file1.read().splitlines()
        if cred_pass in verify:
            global loginsuccess
            loginsuccess = Tk()
            loginsuccess.geometry("400x350")
            loginsuccess.resizable(False, False)
            loginsuccess.title("Login Successful")
            loginsuccess.eval('tk::PlaceWindow . center')

            def login_register_again():
                win = loginsuccess
                window.deiconify()
                win.destroy()
                userbox.delete(0, END)
                passbox.delete(0, END)

            def callback(url):
                webbrowser.open_new_tab(url)

            btn = Button(loginsuccess, bg='green', text='Go back to the main tab to exit program', command=login_register_again)
            btn.pack()

            filename = cred_user
            file = open(filename, 'r')
            f = file.readlines()
            for line in f:
                data = line
                d = Label(loginsuccess, text=data, font=('calibri bold', 9))
                d.pack_configure(anchor="center")

            reg_user_label = Label(loginsuccess, text="Username", font=("arial", 7))
            reg_user_label.place(x=1, y=28)
            reg_pass_label = Label(loginsuccess, text="Password", font=("arial", 7))
            reg_pass_label.place(x=1, y=63)
            fullname_label = Label(loginsuccess, text="Full Name", font=("arial", 7))
            fullname_label.place(x=1, y=96)
            stdntnum_label = Label(loginsuccess, text="Student Number", font=("arial", 7))
            stdntnum_label.place(x=1, y=129)
            age_label = Label(loginsuccess, text="Age", font=("arial", 7))
            age_label.place(x=1, y=164)
            address_label = Label(loginsuccess, text="Address", font=("arial", 7))
            address_label.place(x=1, y=200)
            sem_grade_label = Label(loginsuccess, text="Sem Grade", font=("arial", 7))
            sem_grade_label.place(x=1, y=231)
            link = Label(loginsuccess, text="to access the code click here", font=('Helvetica bold', 8), fg="blue", cursor="hand2")
            link.pack(side="bottom")
            link.bind("<Button-1>", lambda e:
            callback("https://github.com/VITAMINSEAPLUSPLUS/OOP-1-2-VITAMIN-C-"))

            text = Label(loginsuccess, text='Here are the details of your registered account', fg='green', font=('calibri', 14))
            text.place(x=200, y=280, anchor='center')
            window.withdraw()

        else:
            passerror = Label(window, text="Password is incorrect", font="arial 12 italic", fg="red")
            passerror.place(x=151, y=200)
    else:

        usererror = Label(window, text="Username not found", font="arial 12 italic", fg="red")
        usererror.place(x=152, y=200)


def register():
    window.withdraw()
    global userboxreg
    global passboxreg
    global regscreen
    global full_name
    global stdnt_num
    global Age
    global address
    global sem_grade
    global confirm_pass
    global passmsgbox
    regscreen = Tk()
    regscreen.title("Register")
    regscreen.geometry("450x450")
    regscreen.resizable(False, False)
    regscreen.eval('tk::PlaceWindow . center')

    regtitle = Label(regscreen, text="Please fill up this form", font="Arial 11 italic")
    regtitle.place_configure(relx=0.5, rely=0.1, anchor="center")
    reg_user_label = Label(regscreen, text="Username", font=("arial", 11))
    reg_user_label.place(x=85, y=100)
    reg_pass_label = Label(regscreen, text="Password", font=("arial", 11))
    reg_pass_label.place(x=85, y=130)
    confirm_pass_label = Label(regscreen, text="Confirm Password", font=("arial", 11))
    confirm_pass_label.place(x=35, y=160)
    fullname_label = Label(regscreen, text="Full Name", font=("arial", 11))
    fullname_label.place(x=80, y=190)
    stdntnum_label = Label(regscreen, text="Student Number", font=("arial", 11))
    stdntnum_label.place(x=45, y=220)
    Age_label = Label(regscreen, text="Age", font=("arial", 11))
    Age_label.place(x=125, y=250)
    address_label = Label(regscreen, text="Address", font=("arial", 11))
    address_label.place(x=100, y=280)
    sem_grade_label = Label(regscreen, text="Sem Grade", font=("arial", 11))
    sem_grade_label.place(x=80, y=310)
    userboxreg = Entry(regscreen, width=40, bd=2)
    userboxreg.place(x=170, y=100)
    passboxreg = Entry(regscreen, width=40, bd=2, show="*")
    passboxreg.place(x=170, y=130)
    confirm_pass = Entry(regscreen, width=40, bd=2, show="*")
    confirm_pass.place(x=170, y=160)
    full_name = Entry(regscreen, width=40, bd=2)
    full_name.place(x=170, y=190)
    stdnt_num = Entry(regscreen, width=40, bd=2)
    stdnt_num.place(x=170, y=220)
    Age = Entry(regscreen, width=40, bd=2)
    Age.place(x=170, y=250)
    address = Entry(regscreen, width=40, bd=2)
    address.place(x=170, y=280)
    sem_grade = Entry(regscreen, width=10, bd=2)
    sem_grade.place(x=170, y=310)
    buttonreg = Button(regscreen, text="Register", font=('Calibri bold', 15), bd=2, bg='light green', fg="black", command=register_info)
    buttonreg.place(relx=0.5, rely=0.8, anchor='center')


def register_info():
    global error
    user_info = userboxreg.get()
    pass_info = passboxreg.get()
    confirm_pass_info = confirm_pass.get()
    error = Label(regscreen, text="Password don't match", fg='red')
    if confirm_pass_info != pass_info:

        error.place(x=165, y=330)

    else:
        full_name_info = full_name.get()
        stdnt_num_info = stdnt_num.get()
        Age_info = Age.get()
        address_info = address.get()
        sem_grade_info = sem_grade.get()
        file = open(user_info, "w")
        file.write(user_info + "\n")
        file.write(pass_info + "\n")
        file.write(full_name_info + '\n')
        file.write(stdnt_num_info + '\n')
        file.write(Age_info + '\n')
        file.write(address_info + '\n')
        file.write(sem_grade_info)
        file.close()
        tkinter.messagebox.showinfo(title='', message="*Registration Successful*")
        regscreen.withdraw()
        window.deiconify()


title = Label(window, text="Login", font="Verdana 20 bold")
title.place_configure(relx=0.5, rely=0.1, anchor="center")

user_label = Label(window, text="Username*", font=("arial", 11))
user_label.place(x=80, y=100)
pass_label = Label(window, text="Password*", font=("arial", 11))
pass_label.place(x=80, y=130)
userbox = Entry(window, bd=2)
userbox.place(x=170, y=100)
passbox = Entry(window, bd=2, show="*")
passbox.place(x=170, y=130)


regbutton = Button(window, text="Register", bd=2, fg="blue", command=register)
regbutton.place(x=170, y=160)
loginbutton = Button(window, text="Login", bd=2, fg="blue", command=login)
loginbutton.place(x=250, y=160)

window.mainloop()
