import tkinter
from tkinter import *

root = Tk()
root.title("Python Calculator")
root.geometry("380x480")
root.configure(bg="#17161b")

result = "0"
history = "0"

label_history = Label(root, width=100, height=1, text="", font=("arial", 27), relief="solid", justify=RIGHT)
label_history.pack()

label_result = Label(root, width=20, height=1, text="", font=("arial", 27), relief="solid", justify=RIGHT)
label_result.pack()
label_result.config(text="0")

def show(value):
    global result
    global history
    if result == "0":
        if value not in ["+", "-", "/", "*", "%"]:
            if history == "0":
                history = value
            else:
                history = history + value
            result = value
        elif value == ".":
            result = result + value
            history = history + value
        else:
            result = ""
            history = history + value
    else:
        if value == ".":
            result = "0"
            history = history + value
        else:
            result = "0"
            history = history + value
    label_result.config(text=result)
    label_history.config(text=history)

def clear():
    global result
    global history
    result = "0"
    history = "0"
    label_result.config(text=result)
    label_history.config(text=history)

def calculate():
    global result
    global history
    final_result = ""
    
    if result != "":
        try:
            # Handle percentage calculation
            if "%" in history:
                history = history.replace("%", "")
                final_result = str(eval(history) / 100)
            else:
                final_result = str(eval(history))
            
            # Round the result to 10 decimal places
            if '.' in final_result:
                final_result = str(round(float(final_result), 10))
        
        except:
            final_result = "error"
            result = "0"
    
    history = str(final_result)
    label_result.config(text=final_result)
    label_history.config(text=history + "=")

# Buttons
Button(root, text="C", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=120)
Button(root, text="/", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=105, y=120)
Button(root, text="%", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=200, y=120)
Button(root, text="*", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=290, y=120)

Button(root, text="7", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=190)
Button(root, text="8", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=105, y=190)
Button(root, text="9", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=200, y=190)
Button(root, text="+", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=290, y=190)

Button(root, text="4", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=260)
Button(root, text="5", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=105, y=260)
Button(root, text="6", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=200, y=260)
Button(root, text="-", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=290, y=260)

Button(root, text="3", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=10, y=330)
Button(root, text="2", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=105, y=330)
Button(root, text="1", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=200, y=330)

Button(root, text="0", width=9, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=400)
Button(root, text=".", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=200, y=400)

Button(root, text="=", width=4, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=290, y=330)

root.mainloop()