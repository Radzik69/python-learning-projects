import tkinter as tk

class createGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x1000")
        self.root.title("Notepad")

        frame = tk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        self.text_field = tk.Text(frame, wrap='word', cursor="xterm",font=("Consoloas",11))
        self.text_field.pack(side='left', fill='both', expand=True)

        self.text_field_scrollbar = tk.Scrollbar(frame, orient='vertical', command=self.text_field.yview)
        self.text_field_scrollbar.pack(side='right', fill='y')
        self.text_field.config(yscrollcommand=self.text_field_scrollbar.set)



        self.root.mainloop()

createGUI()
