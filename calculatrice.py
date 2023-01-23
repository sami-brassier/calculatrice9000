import tkinter as tk

root = tk.Tk()
root.title("Calculatrice")

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_add():
    first_number = display.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_divide():
    first_number = display.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_sqrt():
    global math
    math = "square root"
    display.delete(0, tk.END)

def button_percentage():
    first_number = display.get()
    global f_num
    global math
    math = "percentage"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_decimal():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + ".")

def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001:
            return guess
        last_guess= guess

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    if math == "addition":
        display.insert(0, f_num + float(second_number))
    if math == "subtraction":
        display.insert(0, f_num - float(second_number))
    if math == "multiplication":
        display.insert(0, f_num * float(second_number))
    if math == "division":
        display.insert(0, f_num / float(second_number))
    if math == "square root":
        display.insert(0, sqrt(float(second_number)))
    if math == "percentage":
        display.insert(0, (f_num * float(second_number))/100)

def button_clear():
    display.delete(0, tk.END)

button_1 = tk.Button(root, text="1", command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", command=lambda: button_click(0))

button_add = tk.Button(root, text="+", command=button_add)
button_subtract = tk.Button(root, text="-", command=button_subtract)
button_multiply = tk.Button(root, text="*", command=button_multiply)
button_divide = tk.Button(root, text="/", command=button_divide)

button_sqrt = tk.Button(root, text="sqrt", command=button_sqrt)
button_percentage = tk.Button(root, text="%", command=button_percentage)

button_decimal = tk.Button(root, text=".", command=button_decimal)

button_equal = tk.Button(root, text="=", command=button_equal)

button_clear = tk.Button(root, text="Clear", command=button_clear)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_sqrt.grid(row=7, column=0)
button_percentage.grid(row=7, column=1)

button_decimal.grid(row=4, column=2)
button_equal.grid(row=5, column=2)
button_clear.grid(row=7, column=2)

display = tk.Entry(root)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()