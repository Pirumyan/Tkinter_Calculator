from tkinter import Tk, Entry, Button

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.entry = Entry(master, width=30, borderwidth=12)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button_text in buttons:
            Button(master, text=button_text, width=5, height=2, command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, value):
        current = self.entry.get()
        if value == 'C':
            self.entry.delete(0, 'end')
        elif value == '=':
            try:
                result = eval(current)
                self.entry.delete(0, 'end')
                self.entry.insert('end', result)
            except:
                self.entry.delete(0, 'end')
                self.entry.insert('end', 'Error')
        else:
            self.entry.insert('end', value)

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
