import tkinter as tk


class Tabuleiro:
        
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha INSPER")
        self.window.geometry("400x500+500+100")
        
    def iniciar(self):
        self.window.mainloop()
        
tab = Tabuleiro()
tab.iniciar()
