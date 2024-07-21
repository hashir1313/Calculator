import tkinter as tk
from tkinter import *
calculation = ""

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def delete():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

icon = PhotoImage(file="calculator.png")
root.iconphoto(False, icon)



frame = tk.Frame(root)

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=4)

btn_1 = tk.Button(root, text="1", font=("Arial", 14), command=lambda: add_to_calculation("1"), width=5)
btn_1.grid(row=2, column=0, columnspan=1, stick="we")
btn_2 = tk.Button(root, text="2", font=("Arial", 14), command=lambda: add_to_calculation("2"), width=5)
btn_2.grid(row=2, column=1, columnspan=1, stick="we")
btn_3 = tk.Button(root, text="3", font=("Arial", 14), command=lambda: add_to_calculation("3"), width=5)
btn_3.grid(row=2, column=2, columnspan=1, stick="we")
btn_4 = tk.Button(root, text="4", font=("Arial", 14), command=lambda: add_to_calculation("4"), width=5)
btn_4.grid(row=3, column=0, columnspan=1, stick="we")
btn_5 = tk.Button(root, text="5", font=("Arial", 14), command=lambda: add_to_calculation("5"), width=5)
btn_5.grid(row=3, column=1, columnspan=1, stick="we")
btn_6 = tk.Button(root, text="6", font=("Arial", 14), command=lambda: add_to_calculation("6"), width=5)
btn_6.grid(row=3, column=2, columnspan=1, stick="we")
btn_7 = tk.Button(root, text="7", font=("Arial", 14), command=lambda: add_to_calculation("7"), width=5)
btn_7.grid(row=4, column=0, columnspan=1, stick="we")
btn_8 = tk.Button(root, text="8", font=("Arial", 14), command=lambda: add_to_calculation("8"), width=5)
btn_8.grid(row=4, column=1, columnspan=1, stick="we")
btn_9 = tk.Button(root, text="9", font=("Arial", 14), command=lambda: add_to_calculation("9"), width=5)
btn_9.grid(row=4, column=2, columnspan=1, stick="we")
btn_0 = tk.Button(root, text="0", font=("Arial", 14), command=lambda: add_to_calculation("0"), width=5)
btn_0.grid(row=5, column=1, columnspan=1, stick="we")
btn_point = tk.Button(root, text=".", font=("Arial", 14), command=lambda: add_to_calculation("."), width=5)
btn_point.grid(row=6, column=1, columnspan=1, stick="we")
btn_left_bracket = tk.Button(root, text="(", font=("Arial", 14), command=lambda: add_to_calculation("("), width=5)
btn_left_bracket.grid(row=5, column=0, columnspan=1, stick="we")
btn_right_bracket = tk.Button(root, text=")", font=("Arial", 14), command=lambda: add_to_calculation(")"), width=5)
btn_right_bracket.grid(row=5, column=2, columnspan=1, stick="we")
btn_equals = tk.Button(root, text="=", font=("Arial", 14), command=lambda: evaluate_calculation(), width=5)
btn_equals.grid(row=2, column=3, columnspan=1, stick="we")
btn_plus = tk.Button(root, text="+", font=("Arial", 14), command=lambda: add_to_calculation("+"), width=5)
btn_plus.grid(row=3, column=3, columnspan=1, stick="we")
btn_minus = tk.Button(root, text="-", font=("Arial", 14), command=lambda: add_to_calculation("-"), width=5)
btn_minus.grid(row=4, column=3, columnspan=1, stick="we")
btn_multiply = tk.Button(root, text="×", font=("Arial", 14), command=lambda: add_to_calculation("*"), width=5)
btn_multiply.grid(row=5, column=3, columnspan=1, stick="we")
btn_divide = tk.Button(root, text="÷", font=("Arial", 14), command=lambda: add_to_calculation("/"), width=5)
btn_divide.grid(row=6, column=3, columnspan=1, stick="we")
btn_clear = tk.Button(root, text="Clear", font=("Arial", 14), command=lambda: clear_field(), width=5)
btn_clear.grid(row=6, column=0, columnspan=1, stick="we")
btn_delete = tk.Button(root, text="Del", font=("Arial", 14), command=lambda: delete(), width=5)
btn_delete.grid(row=6, column=2, columnspan=1, stick="we")


root.mainloop()

