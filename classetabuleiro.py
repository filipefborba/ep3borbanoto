import tkinter as tk
import classejogo


class Tabuleiro():

    
    def __init__(self):
        self.jogo = classejogo.Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x360+100+100")
        self.window.rowconfigure(0, minsize=30, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=100, weight=1)
        self.window.rowconfigure(4, minsize=30, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        self.window.columnconfigure(3, minsize=100, weight=1)

        
    #Criando os Botões:
        
        self.vitorias_X = tk.Label(self.window)
        self.vitorias_X.grid(row=0, column=0, sticky="nsew")
        self.vitorias_X.configure(text="Vitórias de X: {0} ".format(self.jogo.vitórias_x),font='Arial 10', bg='Blue', fg='White')
        
        self.placar = tk.Label(self.window)
        self.placar.grid(row=0, column=1, sticky="nsew")
        self.placar.configure(text= "<- PLACAR ->",font='Arial 10', bg='Black', fg='Green')

        self.vitorias_O = tk.Label(self.window)
        self.vitorias_O.grid(row=0, column=2, sticky="nsew")
        self.vitorias_O.configure(text="Vitórias de O: {0} ".format(self.jogo.vitórias_o), font='Arial 10', bg='Yellow', fg='Black')
        
        
        self.botão0x0 = tk.Button(self.window)
        self.botão0x0.grid(row=1, column=0, sticky="nsew")
        self.botão0x0.configure(command=self.botão0x0_clicado)
         
        self.botão0x1 = tk.Button(self.window)
        self.botão0x1.grid(row=1, column=1, sticky="nsew")
        self.botão0x1.configure(command=self.botão0x1_clicado)
          
        self.botão0x2 = tk.Button(self.window)
        self.botão0x2.grid(row=1, column=2, sticky="nsew")
        self.botão0x2.configure(command=self.botão0x2_clicado)
     
        self.botão1x0 = tk.Button(self.window)
        self.botão1x0.grid(row=2, column=0, sticky="nsew")
        self.botão1x0.configure(command=self.botão1x0_clicado)
         
        self.botão1x1 = tk.Button(self.window)
        self.botão1x1.grid(row=2, column=1, sticky="nsew")
        self.botão1x1.configure(command=self.botão1x1_clicado)
          
        self.botão1x2 = tk.Button(self.window)
        self.botão1x2.grid(row=2, column=2, sticky="nsew")
        self.botão1x2.configure(command=self.botão1x2_clicado)
       
        self.botão2x0 = tk.Button(self.window)
        self.botão2x0.grid(row=3, column=0, sticky="nsew")
        self.botão2x0.configure(command=self.botão2x0_clicado)
         
        self.botão2x1 = tk.Button(self.window)
        self.botão2x1.grid(row=3, column=1, sticky="nsew")
        self.botão2x1.configure(command=self.botão2x1_clicado)
          
        self.botão2x2 = tk.Button(self.window)
        self.botão2x2.grid(row=3, column=2, sticky="nsew")
        self.botão2x2.configure(command=self.botão2x2_clicado)
      
      
      
    #Criando a Label dos turnos:      
        
        
        self.label_turno = tk.Label(self.window)
        self.label_turno.grid(row=4, column=0, columnspan=1, sticky="nsew")
        self.label_turno.configure(text="Turno de : {0}" .format(self.jogo.player), bg='Black', fg='Green',font='Arial 9',)
        
    #Criando Botão de Reiniciar:
        
        self.reiniciar = tk.Button(self.window)
        self.reiniciar.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.reiniciar.configure(text="Reiniciar", font='Arial 24', activeforeground='Green', fg='Red', command=self.restart)
        
        self.label_ganhador = tk.Label(self.window)
        self.label_ganhador.grid(row=4, column=2, columnspan=1, sticky="nsew")
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
        
        
    def clicou(self, i, j):
        print("Turno de: {0} " .format(self.jogo.player))
        print("Botão {0} x {1} clicado" .format(i,j))
        #if         
        #self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
         
############         fg=self.jogo.color
         
    def botão0x0_clicado(self):
        self.clicou(0,0)
        self.botão0x0.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(0,0)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
        
    def botão0x1_clicado(self):
        self.clicou(0,1)
        self.botão0x1.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(0,1)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))        
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
    def botão0x2_clicado(self):
        self.clicou(0,2)
        self.botão0x2.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(0,2)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))          
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',) 
    def botão1x0_clicado(self):
        self.clicou(1,0)
        self.botão1x0.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(1,0)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
    def botão1x1_clicado(self):
        self.clicou(1,1)
        self.botão1x1.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(1,1)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
    def botão1x2_clicado(self):
        self.clicou(1,2)
        self.botão1x2.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(1,2)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)              
    def botão2x0_clicado(self):
        self.clicou(2,0)
        self.botão2x0.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(2,0)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
    def botão2x1_clicado(self):
        self.clicou(2,1)
        self.botão2x1.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(2,1)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
    def botão2x2_clicado(self):
        self.clicou(2,2)
        self.botão2x2.configure(text=self.jogo.player, state= "disabled", font='Arial 100 ')
        self.jogo.recebe_jogada(2,2)
        self.label_turno.configure(text="Turno de: {0}" .format(self.jogo.player))
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
    def iniciar(self):
        self.window.mainloop()
        
    def restart(self):
        self.jogo.limpa_jogadas()
        
        self.botão0x0 = tk.Button(self.window)
        self.botão0x0.grid(row=1, column=0, sticky="nsew")
        self.botão0x0.configure(command=self.botão0x0_clicado)
         
        self.botão0x1 = tk.Button(self.window)
        self.botão0x1.grid(row=1, column=1, sticky="nsew")
        self.botão0x1.configure(command=self.botão0x1_clicado)
          
        self.botão0x2 = tk.Button(self.window)
        self.botão0x2.grid(row=1, column=2, sticky="nsew")
        self.botão0x2.configure(command=self.botão0x2_clicado)
     
        self.botão1x0 = tk.Button(self.window)
        self.botão1x0.grid(row=2, column=0, sticky="nsew")
        self.botão1x0.configure(command=self.botão1x0_clicado)
         
        self.botão1x1 = tk.Button(self.window)
        self.botão1x1.grid(row=2, column=1, sticky="nsew")
        self.botão1x1.configure(command=self.botão1x1_clicado)
          
        self.botão1x2 = tk.Button(self.window)
        self.botão1x2.grid(row=2, column=2, sticky="nsew")
        self.botão1x2.configure(command=self.botão1x2_clicado)
       
        self.botão2x0 = tk.Button(self.window)
        self.botão2x0.grid(row=3, column=0, sticky="nsew")
        self.botão2x0.configure(command=self.botão2x0_clicado)
         
        self.botão2x1 = tk.Button(self.window)
        self.botão2x1.grid(row=3, column=1, sticky="nsew")
        self.botão2x1.configure(command=self.botão2x1_clicado)
          
        self.botão2x2 = tk.Button(self.window)
        self.botão2x2.grid(row=3, column=2, sticky="nsew")
        self.botão2x2.configure(command=self.botão2x2_clicado)
      
      
      
    #Criando a Label dos turnos:      
        
        
        self.label_turno = tk.Label(self.window)
        self.label_turno.grid(row=4, column=0, columnspan=1, sticky="nsew")
        self.label_turno.configure(text="Turno de : {0}" .format(self.jogo.player), bg='Black', fg='Green',font='Arial 9',)
        
    #Criando Botão de Reiniciar:
        
        self.reiniciar = tk.Button(self.window)
        self.reiniciar.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.reiniciar.configure(text="Reiniciar", font='Arial 24', activeforeground='Green', fg='Red', command=self.restart)
        
        self.label_ganhador = tk.Label(self.window)
        self.label_ganhador.grid(row=4, column=2, columnspan=1, sticky="nsew")
        self.label_ganhador.configure(text="Ganhador: {0}" .format(self.jogo.ganhador), bg='Black', fg='Green',font='Arial 9',)
        self.vitorias_X.configure(text="Vitórias de X: {0} ".format(self.jogo.vitórias_x), bg='Blue', fg='White')
        self.vitorias_O.configure(text="Vitórias de O:  {0} ".format(self.jogo.vitórias_o), bg='Yellow', fg='Black')


            
            
jogodavelha = Tabuleiro()
jogodavelha.iniciar()
