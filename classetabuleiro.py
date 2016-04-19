import tkinter as tk


class Tabuleiro:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha 13")
        self.window.geometry("300x350")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        self.player = ["X","O"]

        
    #Criando os Botões:
        
        self.botão0x0 = tk.Button(self.window)
        self.botão0x0.grid(row=0, column=0, sticky="nsew")
        self.botao0x0.configure(command = self.recebe_jogada(0,0))
         
        self.botão0x1 = tk.Button(self.window)
        self.botão0x1.grid(row=0, column=1, sticky="nsew")
        self.botao0x1.configure(command = self.recebe_jogada(0,1))
          
        self.botão0x2 = tk.Button(self.window)
        self.botão0x2.grid(row=0, column=2, sticky="nsew")
        self.botao0x2.configure(command = self.recebe_jogada(0,2))
     
        self.botão1x0 = tk.Button(self.window)
        self.botão1x0.grid(row=1, column=0, sticky="nsew")
        self.botao1x0.configure(command = self.recebe_jogada(1,0))
         
        self.botão1x1 = tk.Button(self.window)
        self.botão1x1.grid(row=1, column=1, sticky="nsew")
        self.botao1x1.configure(command = self.recebe_jogada(1,1))
        
        self.botão1x2 = tk.Button(self.window)
        self.botão1x2.grid(row=1, column=2, sticky="nsew")
        self.botao1x2.configure(command = self.recebe_jogada(1,2))
       
        self.botão2x0 = tk.Button(self.window)
        self.botão2x0.grid(row=2, column=0, sticky="nsew")
        self.botao2x0.configure(command = self.recebe_jogada(2,0))
         
        self.botão2x1 = tk.Button(self.window)
        self.botão2x1.grid(row=2, column=1, sticky="nsew")
        self.botao2x1.configure(command = self.recebe_jogada(2,1))
          
        self.botão2x2 = tk.Button(self.window)
        self.botão2x2.grid(row=2, column=2, sticky="nsew")
        self.botao2x2.configure(command = self.recebe_jogada(2,2))
      
      
    #Criando a Label dos turnos:      
      
        turno = tk.Label(self.window)
        turno.configure(text="Turno de: %s" % self.player[x])
        turno.grid(row=3, columnspan=3, sticky="nsew")
        
    def iniciar(self):
        self.window.mainloop()
        
tab = Tabuleiro()
tab.iniciar()

    def iniciar(self):
        self.window.mainloop()
        
tab = Tabuleiro()
tab.iniciar()
