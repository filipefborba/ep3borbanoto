import tkinter as tk


class Tabuleiro:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x350")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)

        
    #Criando os Botões:
        
        botão0x0 = tk.Button(self.window)
        botão0x0.grid(row=0, column=0, sticky="nsew")
         
        botão0x1 = tk.Button(self.window)
        botão0x1.grid(row=0, column=1, sticky="nsew")
          
        botão0x2 = tk.Button(self.window)
        botão0x2.grid(row=0, column=2, sticky="nsew")
     
        botão1x0 = tk.Button(self.window)
        botão1x0.grid(row=1, column=0, sticky="nsew")
         
        botão1x1 = tk.Button(self.window)
        botão1x1.grid(row=1, column=1, sticky="nsew")
          
        botão1x2 = tk.Button(self.window)
        botão1x2.grid(row=1, column=2, sticky="nsew")
       
        botão2x0 = tk.Button(self.window)
        botão2x0.grid(row=2, column=0, sticky="nsew")
         
        botão2x1 = tk.Button(self.window)
        botão2x1.grid(row=2, column=1, sticky="nsew")
          
        botão2x2 = tk.Button(self.window)
        botão2x2.grid(row=2, column=2, sticky="nsew")
      
      
    #Criando a Label dos turnos:      
      
        turno = tk.Label(self.window)
        turno.configure(text="Turno de: ")
        turno.grid(row=3, columnspan=3, sticky="nsew")
        
    def iniciar(self):
        self.window.mainloop()
        
tab = Tabuleiro()
tab.iniciar()
