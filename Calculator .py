# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator-Yashashree Bedmutha ')
frame = tk.Frame(master=window, bg="Black", padx=20)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=10, width=30)
entry.grid(row=0, column=0, columnspan=7, ipady=6, pady=6)


def myclick(number):
 entry.insert(tk.END, number)


def equal():
 try:
  y = str(eval(entry.get()))
  entry.delete(0, tk.END)
  entry.insert(0, y)
 except:
  tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
 entry.delete(0, tk.END)


b_1 = tk.Button(master=frame, text='1', padx=15,pady=5, width=3, command=lambda: myclick(1))
b_1.grid(row=1, column=0, pady=2)
b_2 = tk.Button(master=frame, text='2', padx=15,pady=5, width=3, command=lambda: myclick(2))
b_2.grid(row=1, column=1, pady=2)
b_3 = tk.Button(master=frame, text='3', padx=15,pady=5, width=3, command=lambda: myclick(3))
b_3.grid(row=1, column=2, pady=2)
b_4 = tk.Button(master=frame, text='4', padx=15,pady=5, width=3, command=lambda: myclick(4))
b_4.grid(row=2, column=0, pady=2)
b_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5))
b_5.grid(row=2, column=1, pady=2)
b_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6))
b_6.grid(row=2, column=2, pady=2)
b_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7))
b_7.grid(row=3, column=0, pady=2)
b_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8))
b_8.grid(row=3, column=1, pady=2)
b_9 = tk.Button(master=frame, text='9', padx=15,pady=5, width=3, command=lambda: myclick(9))
b_9.grid(row=3, column=2, pady=2)
b_0 = tk.Button(master=frame, text='0', padx=15,pady=5, width=3, command=lambda: myclick(0))
b_0.grid(row=4, column=1, pady=2)

b_add = tk.Button(master=frame, text="+", padx=15,pady=5, width=3, command=lambda: myclick('+'))
b_add.grid(row=5, column=0, pady=2)

b_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
b_subtract.grid(row=5, column=1, pady=2)

b_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
b_multiply.grid(row=5, column=2, pady=2)

b_div = tk.Button(master=frame, text="/", padx=15,pady=5, width=3, command=lambda: myclick('/'))
b_div.grid(row=6, column=0, pady=2)

b_mod = tk.Button(master=frame, text="%", padx=15,pady=5, width=3, command=lambda: myclick('%'))
b_mod.grid(row=7, column=0, pady=2)

b_pov = tk.Button(master=frame, text="**", padx=15,pady=5, width=3, command=lambda: myclick('**'))
b_pov.grid(row=7, column=1, pady=2)

b_brk1 = tk.Button(master=frame, text="(", padx=15,pady=5, width=3, command=lambda: myclick('('))
b_brk1.grid(row=6, column=2, pady=2)

b_brk2 = tk.Button(master=frame, text=")", padx=15,pady=5, width=3, command=lambda: myclick(')'))
b_brk2.grid(row=6, column=3, pady=2)

b_clear = tk.Button(master=frame, text="clear",padx=15, pady=5, width=10, command=clear)
b_clear.grid(row=7, column=2, columnspan=2, pady=2)

b_equal = tk.Button(master=frame, text="=", padx=15,pady=5, width=9, command=equal)
b_equal.grid(row=8, column=0, columnspan=3, pady=2)

window.mainloop()
