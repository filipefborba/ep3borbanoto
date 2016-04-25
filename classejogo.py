import numpy as np
import random

class Jogo():
  def __init__(self):
      self.players = ["X","O"," "]
      self.ganhador = "-"
      self.player = self.players
      self.sorteia_iniciante()
      self.matriz = np.zeros([3,3])
      self.vitórias_x = 0
      self.vitórias_o = 0
      
  def iniciar(self):
    self.window.mainloop()
    
  def sorteia_iniciante(self):
  #Se "a" for 0 o jogador X inicia, caso for 1, o jogador O inicia.
    a = random.randint(0,1)
    if a == 0:
        self.player = self.players[0]
    else:
        self.player = self.players[1]
    
  def recebe_jogada(self, linha, coluna):
    verifica = self.verifica_ganhador()
    #Enquanto não há ganhador (verifica = -1), as jogadas são registradas.
    if verifica == -1:
        if self.matriz[linha][coluna] == 0:
            if self.player == self.players[0]: 
                self.matriz[linha][coluna] = 1
                print(self.matriz)
                print()
                self.player = self.players[1]
                verifica = self.verifica_ganhador()
                
            elif self.player == self.players[1]:
                self.matriz[linha][coluna] = 9
                print(self.matriz)
                print()
                self.player = self.players[0]
                verifica = self.verifica_ganhador()
    elif verifica == 2:
        self.vitórias_o -=1
    elif verifica == 1:
        self.vitórias_x -=1
    else:
        pass
    
  def verifica_ganhador(self):
    #O computador somará as linhas, colunas e diagonais da matriz registrada
    #pelos botões. X tem o valor de 1 e O tem o valor de 9.
    #Caso alguém ganhe, será adicionado um ponto no seu placar após reiniciar.
    soma_colunas = np.sum(self.matriz, 0)
    soma_linhas = np.sum(self.matriz, 1)
    
    if soma_colunas[0] == 27 or soma_linhas[0] == 27\
    or soma_colunas[1] == 27 or soma_linhas[1] == 27 \
    or soma_colunas[2] == 27 or soma_linhas[2] == 27 \
    or self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2] == 27 \
    or self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2] == 27:
      
        self.ganhador=" O "
        self.player = self.players[2]
        self.vitórias_o +=1
        print(self.vitórias_o)
        return 2
        
    elif soma_colunas[0] == 3 or soma_linhas[0] == 3\
    or soma_colunas[1] == 3 or soma_linhas[1] == 3 \
    or soma_colunas[2] == 3 or soma_linhas[2] == 3 \
    or self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2] == 3 \
    or self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2] == 3:  
        
        self.ganhador = " X "
        self.player = self.players[2]
        self.vitórias_x += 1
        print(self.vitórias_x)
        return 1
    
    elif np.sum(self.matriz) == 49 or np.sum(self.matriz) == 41:
        print()
        self.ganhador = "Deu velha!"
        self.player = self.players[2]
        return 0
    else:
        return -1
        
  def limpa_jogadas(self):
    self.matriz = np.zeros([3,3])
    self.sorteia_iniciante()
    self.ganhador = "-"