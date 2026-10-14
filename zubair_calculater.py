import tkinter as tk
from tkinter import messagebox
import math


# helper to create visually square/circular-like buttons
def make_button(master, text, bg, fg, cmd, font=("Arial",16)):
    b = tk.Button(master, text=text, bg=bg, fg=fg, font=font, bd=0, relief="ridge", command=cmd)
    # width/height tuned to give a circular/square look
    b.config(width=6, height=2)
    return b

class ZubairCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Zubair Calculator")
        self.root.geometry("420x640")
        self.root.configure(bg="black")

        self.expr = ""                 # expression string
        self.display_var = tk.StringVar()

        # top display (shared between modes)
        display_frame = tk.Frame(self.root, bg="black")
        display_frame.pack(side=tk.TOP, fill=tk.X, padx=8, pady=10)

        self.display = tk.Entry(display_frame, textvariable=self.display_var,
                                font=("Arial", 28, "bold"), bd=0,
                                justify=tk.RIGHT, bg="black", fg="white", insertbackground="white")
        self.display.pack(fill=tk.X, ipady=12)

        # footer
        footer = tk.Label(self.root, text="Developed by Zubair Safi", fg="white", bg="black", font=("Arial",10))
        footer.pack(side=tk.BOTTOM, pady=6)

        # container for frames (main + scientific)
        container = tk.Frame(self.root, bg="black")
        container.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0,8))

        # two stacked frames (raise to switch)
        self.main_frame = tk.Frame(container, bg="black")
        self.sci_frame  = tk.Frame(container, bg="black")

        for f in (self.main_frame, self.sci_frame):
            f.grid(row=0, column=0, sticky="nsew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # key bindings
        self.root.bind("<Key>", self.on_key)

        # build frames
        self.build_main()
        self.build_scientific()

        # show main first
        self.show_frame(self.main_frame)

    def show_frame(self, frame):
        frame.tkraise()

    # ------------ input helpers ------------
    def add_char(self, ch):
        self.expr += str(ch)
        self.display_var.set(self.expr)

    def clear_all(self):
        self.expr = ""
        self.display_var.set("")

    def backspace(self):
        self.expr = self.expr[:-1]
        self.display_var.set(self.expr)

    def press_percent(self):
        """Smart % button: percentage if last char is number, else modulo"""
        if self.expr and self.expr[-1].isdigit():
            self.expr += "/100"
        else:
            self.expr += "%"
        self.display_var.set(self.expr)

    def on_key(self, event):
        # allow digits, operators, ., parentheses, enter, backspace
        c = event.char
        if c in "0123456789.+-*/()":
            self.add_char(c)
        elif event.keysym == "Return":
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.backspace()

    # ------------ evaluation with safe preprocessing ------------
    def preprocess(self, expr: str) -> str:
        e = expr
        # Replace human-friendly function names -> math.* usage.
        e = e.replace("sin(", "math.sin(math.radians(")
        e = e.replace("cos(", "math.cos(math.radians(")
        e = e.replace("tan(", "math.tan(math.radians(")
        e = e.replace("log(", "math.log10(")        # user presses 'log('
        e = e.replace("factorial(", "math.factorial(")
        if "__" in e:
            raise ValueError("Invalid input")
        return e

    def evaluate(self):
        self.evaluate_alias()

    def evaluate_alias(self):
        if not self.expr.strip():
            return
        try:
            processed = self.preprocess(self.expr)
            result = eval(processed, {"__builtins__": None, "math": math}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expr = str(result)
            self.display_var.set(self.expr)
        except Exception as ex:
            messagebox.showerror("Error", "Invalid input or math error")

    # ------------ Main frame layout ------------
    def build_main(self):
        f = self.main_frame
        f.configure(bg="black")

        for r in range(5):
            f.grid_rowconfigure(r, weight=1)
        for c in range(4):
            f.grid_columnconfigure(c, weight=1)

        layout = [
            ['C', '⌫', 'Scientific', '/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['0','.','=','%']   # <-- added % here
        ]

        for r, row in enumerate(layout):
            for c, key in enumerate(row):
                if key == '':
                    lbl = tk.Label(f, bg="black")
                    lbl.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)
                    continue

                if key == 'C':
                    btn = make_button(f, key, bg="orange", fg="black", cmd=self.clear_all)
                elif key == '⌫':
                    btn = make_button(f, key, bg="orange", fg="black", cmd=self.backspace)
                elif key == 'Scientific':
                    btn = make_button(f, key, bg="red", fg="white", cmd=lambda: self.show_frame(self.sci_frame))
                elif key == '%':
                    btn = make_button(f, key, bg="orange", fg="black", cmd=self.press_percent)
                elif key in ['+','-','*','/','=']:
                    if key == '=':
                        btn = make_button(f, key, bg="orange", fg="black", cmd=self.evaluate_alias)
                    else:
                        btn = make_button(f, key, bg="orange", fg="black", cmd=lambda x=key: self.add_char(x))
                else:
                    btn = make_button(f, key, bg="white", fg="black", cmd=lambda x=key: self.add_char(x))

                btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)

    # ------------ Scientific frame layout ------------
    def build_scientific(self):
        f = self.sci_frame
        f.configure(bg="black")

        rows = 8
        cols = 4
        for r in range(rows):
            f.grid_rowconfigure(r, weight=1)
        for c in range(cols):
            f.grid_columnconfigure(c, weight=1)

        layout = [
            ['C','⌫','Main','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['0','.','=','x²'],
            ['x³','x^y','√x','∛x'],
            ['sin','cos','tan','log'],
            ['!','(',')','%']  # <-- added % here
        ]

        for r, row in enumerate(layout):
            for c, key in enumerate(row):
                if key == '':
                    lbl = tk.Label(f, bg="black")
                    lbl.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)
                    continue

                if key == 'C':
                    btn = make_button(f, key, bg="orange", fg="black", cmd=self.clear_all)
                elif key == '⌫':
                    btn = make_button(f, key, bg="orange", fg="black", cmd=self.backspace)
                elif key == 'Main':
                    btn = make_button(f, key, bg="red", fg="white", cmd=lambda: self.show_frame(self.main_frame))
                elif key == '%':
                    btn = make_button(f, key, bg="orange", fg="black", cmd=self.press_percent)
                elif key in ['+','-','*','/','=']:
                    if key == '=':
                        btn = make_button(f, key, bg="orange", fg="black", cmd=self.evaluate_alias)
                    else:
                        btn = make_button(f, key, bg="orange", fg="black", cmd=lambda x=key: self.add_char(x))
                elif key in ['x²','x³','x^y','√x','∛x','sin','cos','tan','log','!','(',')']:
                    btn = make_button(f, key, bg="orange", fg="black", cmd=lambda x=key: self.scientific_press(x))
                else:
                    btn = make_button(f, key, bg="white", fg="black", cmd=lambda x=key: self.add_char(x))

                btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)

    def scientific_press(self, key):
        try:
            if key == 'x²':
                self.add_char("**2")
            elif key == 'x³':
                self.add_char("**3")
            elif key == 'x^y':
                self.add_char("**")
            elif key == '√x':
                self.add_char("**0.5")
            elif key == '∛x':
                self.add_char("**(1/3)")
            elif key == 'sin':
                self.add_char("sin(")
            elif key == 'cos':
                self.add_char("cos(")
            elif key == 'tan':
                self.add_char("tan(")
            elif key == 'log':
                self.add_char("log(")
            elif key == '!':
                self.add_char("factorial(")
            elif key == '(' or key == ')':
                self.add_char(key) 
            else:
                self.add_char(key)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")

# ----------------------------
# Run the application
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ZubairCalculator(root)
    root.mainloop()
