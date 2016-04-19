import tkinter as tk
import classejogo


class Tabuleiro():

    
    def __init__(self):
        self.jogo = classejogo.Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x350")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=30, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)

        
    #Criando os Botões:
        
        self.botão0x0 = tk.Button(self.window)
        self.botão0x0.grid(row=0, column=0, sticky="nsew")
        self.botão0x0.configure(command=self.botão0x0_clicado)
         
        self.botão0x1 = tk.Button(self.window)
        self.botão0x1.grid(row=0, column=1, sticky="nsew")
        self.botão0x1.configure(command=self.botão0x1_clicado)
          
        self.botão0x2 = tk.Button(self.window)
        self.botão0x2.grid(row=0, column=2, sticky="nsew")
        self.botão0x2.configure(command=self.botão0x2_clicado)
     
        self.botão1x0 = tk.Button(self.window)
        self.botão1x0.grid(row=1, column=0, sticky="nsew")
        self.botão1x0.configure(command=self.botão1x0_clicado)
         
        self.botão1x1 = tk.Button(self.window)
        self.botão1x1.grid(row=1, column=1, sticky="nsew")
        self.botão1x1.configure(command=self.botão1x1_clicado)
          
        self.botão1x2 = tk.Button(self.window)
        self.botão1x2.grid(row=1, column=2, sticky="nsew")
        self.botão1x2.configure(command=self.botão1x2_clicado)
       
        self.botão2x0 = tk.Button(self.window)
        self.botão2x0.grid(row=2, column=0, sticky="nsew")
        self.botão2x0.configure(command=self.botão2x0_clicado)
         
        self.botão2x1 = tk.Button(self.window)
        self.botão2x1.grid(row=2, column=1, sticky="nsew")
        self.botão2x1.configure(command=self.botão2x1_clicado)
          
        self.botão2x2 = tk.Button(self.window)
        self.botão2x2.grid(row=2, column=2, sticky="nsew")
        self.botão2x2.configure(command=self.botão2x2_clicado)
      
    #Criando a Label dos turnos:      
      
        self.label_turno = tk.Label(self.window)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_turno.grid(row=3, columnspan=3, sticky="nsew")
        
        
    def clicou(self, i, j):
        print("Turno de: {0} " .format(self.jogo.player))
        print("Botão {0} x {1} clicado" .format(i,j))
        #if         
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
         
            
    def botão0x0_clicado(self):
        self.clicou(0,0)
        self.botão0x0.configure(text=self.jogo.player)
        self.botão0x0.configure(state= "disabled")
        self.botão0x0.configure(font='Arial 100 ' )
        self.jogo.recebe_jogada(0,0)
        
        
    def botão0x1_clicado(self):
        self.clicou(0,1)
        self.botão0x1.configure(text=self.jogo.player)
        self.botão0x1.configure(state= "disabled")
        self.botão0x1.configure(font='Arial 100' )
        self.jogo.recebe_jogada(0,1)
        
    def botão0x2_clicado(self):
        self.clicou(0,2)
        self.botão0x2.configure(text=self.jogo.player)
        self.botão0x2.configure(state= "disabled")
        self.botão0x2.configure(font='Arial 100 ' )
        self.jogo.recebe_jogada(0,2)

################          
          
    def botão1x0_clicado(self):
        self.clicou(1,0)
        self.botão1x0.configure(text=self.jogo.player)
        self.botão1x0.configure(state= "disabled")
        self.botão1x0.configure(font='Arial 100' )
        self.jogo.recebe_jogada(1,0)
        
    def botão1x1_clicado(self):
        self.clicou(1,1)
        self.botão1x1.configure(text=self.jogo.player)
        self.botão1x1.configure(state= "disabled")
        self.botão1x1.configure(font='Arial 100' )
        self.jogo.recebe_jogada(1,1)
        
    def botão1x2_clicado(self):
        self.clicou(1,2)
        self.botão1x2.configure(text=self.jogo.player)
        self.botão1x2.configure(state= "disabled")
        self.botão1x2.configure(font='Arial 100' )
        self.jogo.recebe_jogada(1,2)
            
################            
            
    def botão2x0_clicado(self):
        self.clicou(2,0)
        self.botão2x0.configure(text=self.jogo.player)
        self.botão2x0.configure(state= "disabled")
        self.botão2x0.configure(font='Arial 100' )
        self.jogo.recebe_jogada(2,0)
        
    def botão2x1_clicado(self):
        self.clicou(2,1)
        self.botão2x1.configure(text=self.jogo.player)
        self.botão2x1.configure(state= "disabled")
        self.botão2x1.configure(font='Arial 100' )
        self.jogo.recebe_jogada(2,1)
        
    def botão2x2_clicado(self):
        self.clicou(2,2)
        self.botão2x2.configure(text=self.jogo.player)
        self.botão2x2.configure(state= "disabled")
        self.botão2x2.configure(font='Arial 100' )
        self.jogo.recebe_jogada(2,2)
        
jogodavelha = Tabuleiro()
jogodavelha.window.mainloop()
