from tkinter import *
expression=''

def press(value):
   global expression
   expression+=str(value)
   equation.set(expression)


def equalpress():
   try:
      global expression
      total = str(eval(expression))
      equation.set(total)
      expression = ""
   except:
      equation.set(" error ")
      expression = ""

def clear():
   global expression
   expression = ""
   equation.set("")
   equation.set("")

window = Tk()
window.configure(background="black")
window.title("Calculator")
window.geometry("400x350")
equation = StringVar()
expression_field = Entry(window, width=16, bd=6, font=('', 32), bg='dark Gray', textvariable=equation)
expression_field.grid(columnspan=4)
window.resizable(False, False)
equation.set('ENTER A NUMBER')

oprtn1=Button(window,width=12,height=4,text='+',bg='black',fg='white',command=lambda: press('+'))
oprtn1.grid(column=0,row=1)
btn1=Button(window,width=12,height=4,text='7',bg='black',fg='white',command=lambda: press(7))
btn1.grid(column=1,row=1)
btn2=Button(window,width=12,height=4,text='8',bg='black',fg='white',command=lambda: press(8))
btn2.grid(column=2,row=1)
btn3=Button(window,width=12,height=4,text='9',bg='black',fg='white',command=lambda: press(9))
btn3.grid(column=3,row=1)
oprtn2=Button(window,width=12,height=4,text='-',bg='black',fg='white',command=lambda: press('-'))
oprtn2.grid(column=0,row=2)
btn4=Button(window,width=12,height=4,text='4',bg='black',fg='white',command=lambda: press(4))
btn4.grid(column=1,row=2)
btn5=Button(window,width=12,height=4,text='5',bg='black',fg='white',command=lambda: press(5))
btn5.grid(column=2,row=2)
btn6=Button(window,width=12,height=4,text='6',bg='black',fg='white',command=lambda: press(6))
btn6.grid(column=3,row=2)
oprtn3=Button(window,width=12,height=4,text='x',bg='black',fg='white',command=lambda: press('*'))
oprtn3.grid(column=0,row=3)
btn7=Button(window,width=12,height=4,text='1',bg='black',fg='white',command=lambda: press(1))
btn7.grid(column=1,row=3)
btn8=Button(window,width=12,height=4,text='2',bg='black',fg='white',command=lambda: press(2))
btn8.grid(column=2,row=3)
btn9=Button(window,width=12,height=4,text='3',bg='black',fg='white',command=lambda: press(3))
btn9.grid(column=3,row=3)
oprtn4=Button(window,width=12,height=4,text='/',bg='black',fg='white',command=lambda: press('/'))
oprtn4.grid(column=0,row=4)
btn10=Button(window,width=12,height=4,text='0',bg='black',fg='white',command=lambda: press(0))
btn10.grid(column=1,row=4)
btn11=Button(window,width=12,height=4,text='=',bg='black',fg='white',command=equalpress)
btn11.grid(column=2,row=4)
btn12=Button(window,width=12,height=4,text='clear',bg='red',fg='orange',command=clear)
btn12.grid(column=3,row=4)

mainloop()