import numpy as np
import random

class Jogo():
  def __init__(self):
      self.players = ["X","O"]
      self.player = self.players
      self.sorteia_iniciante()
      self.matriz = np.zeros([3,3])
      
  def iniciar(self):
    self.window.mainloop()
    
  def sorteia_iniciante(self):
    a = random.randint(0,1)
    #Se o clique for 0 o jogador X inicia, caso for 1, o jogador O inicia.
    if a == 0:
        self.player = self.players[0]
    else:
        self.player = self.players[1]
    
  def recebe_jogada(self, linha, coluna):
    verifica = self.verifica_ganhador()
    
    #Registrar jogada
    if verifica == -1:
        if self.matriz[linha][coluna] == 0:
            if self.player == self.players[0]:
                self.matriz[linha][coluna] = 1
                print(self.matriz)
                self.player = self.players[1]
            elif self.player == self.players[1]:
                self.matriz[linha][coluna] = 9
                print(self.matriz)
                self.player = self.players[0]
    elif verifica >= 0:
        
        pass
  def verifica_ganhador(self):
    #Verificação das possíveis vitórias
    #Verificar quem ganha, -1 indica que o jogo está em andamento
    
    #Colocar sleep e depos limpa_jogadas? ##################################
#        print("Deu Velha!")
#        return 0
#        print("O jogador 1 (X) venceu!")
#        return 1
        #print("O jogador 2 (O) venceu!")

    if self.matriz[0][0] + self.matriz[0][1] + self.matriz[0][2] == 27 or self.matriz[1][0] + self.matriz[1][1] + self.matriz[1][2] == 27 \
    or self.matriz[2][0] + self.matriz[2][1] + self.matriz[2][2] == 27 or self.matriz[0][0] + self.matriz[1][0] + self.matriz[2][0] == 27 \
    or self.matriz[0][1] + self.matriz[1][1] + self.matriz[2][1] == 27 or self.matriz[0][2] + self.matriz[1][2] + self.matriz[2][2] == 27 \
    or self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2] == 27 or self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2] == 27:
        print("O jogador 2 (O) venceu!")
        return 2
        
    elif  self.matriz[0][0] + self.matriz[0][1] + self.matriz[0][2] == 3 or self.matriz[1][0] + self.matriz[1][1] + self.matriz[1][2] == 3 \
    or self.matriz[2][0] + self.matriz[2][1] + self.matriz[2][2] == 3 or self.matriz[0][0] + self.matriz[1][0] + self.matriz[2][0] == 3 \
    or self.matriz[0][1] + self.matriz[1][1] + self.matriz[2][1] == 3 or self.matriz[0][2] + self.matriz[1][2] + self.matriz[2][2] == 3 \
    or self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2] == 3 or self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2] == 3:    
        print("O jogador 1 (X) venceu!")
        return 1
    
    elif np.sum(self.matriz) == 49 or np.sum(self.matriz) == 41:
        print("Deu velha!")
        return 0
    else:         #return 2
        return -1
        
  def limpa_jogadas(self):
    #Reiniciar os botões, cliques, etc.
    #Podemos fazer um botão pra isso
    verifica = self.verifica_ganhador()
    
    #Reiniciar registro de jogadas
    self.matriz = np.zeros([3,3])
    
    #Reiniciar botões
    
    #Reiniciar jogador
    if verifica == 1:
        self.player = self.players[0]
    elif verifica == 2:
        self.player = self.players[1]
    else:
        self.sorteia_iniciante()
        
    
"""Método para limpar as jogadas, ou seja, reinicia o jogo (não
limpará a tela – lembre-se que a classe Jogo não tem acesso à classe
Tabuleiro), mantendo a vez do jogador."""
