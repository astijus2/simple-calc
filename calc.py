import tkinter as tk
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=70, height=50, radius=20, bg="white", fg="black"):
        # Create a canvas that matches the window background (#333333) so it looks transparent
        super().__init__(parent, width=width, height=height, bg="#333333", highlightthickness=0)
        self.command = command
        
        # Draw the rounded shape (4 corners + 2 rectangles)
        self.create_oval(0, 0, radius*2, radius*2, fill=bg, outline=bg)
        self.create_oval(width-radius*2, 0, width, radius*2, fill=bg, outline=bg)
        self.create_oval(0, height-radius*2, radius*2, height, fill=bg, outline=bg)
        self.create_oval(width-radius*2, height-radius*2, width, height, fill=bg, outline=bg)
        self.create_rectangle(radius, 0, width-radius, height, fill=bg, outline=bg)
        self.create_rectangle(0, radius, width, height-radius, fill=bg, outline=bg)
        
        # Add the text in the center
        self.text_id = self.create_text(width/2, height/2, text=text, fill=fg, font=("Arial", 12, "bold"))
        
        # Bind click events
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event): self.move(self.text_id, 1, 1) # simple click effect
    def _on_release(self, event): self.move(self.text_id, -1, -1); self.command() if self.command else None

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#333333")  
    root.title("Simple Calculator")
    root.geometry("400x550")

    display = tk.StringVar()
    entry = tk.Entry(root, textvariable=display, highlightthickness=2, highlightbackground="white", highlightcolor="white")
    entry.grid(columnspan=4, ipadx=70, ipady=10, pady=20)

    # Number buttons
    btn1 = RoundedButton(root, text='1', fg='black', bg='white', command=lambda: press(1))
    btn1.grid(row=2, column=0, padx=5, pady=5)
    btn2 = RoundedButton(root, text='2', fg='black', bg='white', command=lambda: press(2))
    btn2.grid(row=2, column=1, padx=5, pady=5)
    btn3 = RoundedButton(root, text='3', fg='black', bg='white', command=lambda: press(3))
    btn3.grid(row=2, column=2, padx=5, pady=5)
    btn4 = RoundedButton(root, text='4', fg='black', bg='white', command=lambda: press(4))
    btn4.grid(row=3, column=0, padx=5, pady=5)
    btn5 = RoundedButton(root, text='5', fg='black', bg='white', command=lambda: press(5))
    btn5.grid(row=3, column=1, padx=5, pady=5)
    btn6 = RoundedButton(root, text='6', fg='black', bg='white', command=lambda: press(6))
    btn6.grid(row=3, column=2, padx=5, pady=5)
    btn7 = RoundedButton(root, text='7', fg='black', bg='white', command=lambda: press(7))
    btn7.grid(row=4, column=0, padx=5, pady=5)
    btn8 = RoundedButton(root, text='8', fg='black', bg='white', command=lambda: press(8))
    btn8.grid(row=4, column=1, padx=5, pady=5)
    btn9 = RoundedButton(root, text='9', fg='black', bg='white', command=lambda: press(9))
    btn9.grid(row=4, column=2, padx=5, pady=5)
    btn0 = RoundedButton(root, text='0', fg='black', bg='white', command=lambda: press(0))
    btn0.grid(row=5, column=0, padx=5, pady=5)

    # Operator buttons
    plus = RoundedButton(root, text='+', fg='black', bg='white', command=lambda: press('+'))
    plus.grid(row=2, column=3, padx=5, pady=5)
    minus = RoundedButton(root, text='-', fg='black', bg='white', command=lambda: press('-'))
    minus.grid(row=3, column=3, padx=5, pady=5)
    mult = RoundedButton(root, text='*', fg='black', bg='white', command=lambda: press('*'))
    mult.grid(row=4, column=3, padx=5, pady=5)
    div = RoundedButton(root, text='/', fg='black', bg='white', command=lambda: press('/'))
    div.grid(row=5, column=3, padx=5, pady=5)

    # Other buttons
    eq = RoundedButton(root, text='=', fg='black', bg='white', command=equal)
    eq.grid(row=5, column=2, padx=5, pady=5)
    clr = RoundedButton(root, text='Clear', fg='black', bg='white', command=clear)
    clr.grid(row=5, column=1, padx=5, pady=5)
    dot = RoundedButton(root, text='.', fg='black', bg='white', command=lambda: press('.'))
    dot.grid(row=6, column=0, padx=5, pady=5)

    root.mainloop()