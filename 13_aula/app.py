import tkinter as tk
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.root.geometry("300x300")
     

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()