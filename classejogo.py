import numpy as np

class Jogo(Tabuleiro):
  def __init__(self):

  def iniciar(self):
    self.window.mainloop()
    
  def apertou(self):
    #Evento: necessário para registrar a jogada, add na lista e verificar se ganhou.
    self.button.configure(text="O")
    self.button.configure(font="Calibri 100 bold")
    
  def sorteia_iniciante():
    a = random.randint(0,1)
    #Se o clique for 0 o jogador X inicia, caso for 1, o jogador O inicia.
    if a == 0:
        self.player = self.player[0]
    else:
        self.player = self.player[1]
    
  def verifica_ganhador():
    #Verificação das possíveis vitórias
    for i in range(3):
    
    #Verificar quem ganha, -1 indica que o jogo está em andamento
    if 
        print("Deu Velha!")
        return 0
    elif listaX in vitoria:
        print("O jogador 1 (X) venceu!")
        return 1
    elif listaO in vitoria:
        print("O jogador 2 (O) venceu!")
        return 2
    else:
        return -1

""" Método para verificar se o jogo acabou. A função deve
retornar 0 em caso de empate, 1 caso o X seja o vencedor, 2 caso o O seja o
vencedor ou -1 caso contrário. ListaX,ListaO = posições do X/O no tabuleiro."""

def recebe_jogada(linha, coluna):
    verifica_ganhador() = verifica
    matrizX = np.zeros([3,3])
    matrizO = np.zeros([3,3])
    
    #Registrar jogada
    while True:
        if verifica == -1:
            if matrizX[linha][coluna] == 0:
                if self.player == 0:
                    self.button.configure(text=self.player[0])
                    matrizX[linha][coluna] = 1
                    self.player = self.player[1]
                elif self.player == 1:
                    self.button.configure(text=self.player[1])
                    matrizO[linha][coluna] = 0
                    self.player = self.player[0]
        if verifica >= 0:
            break
        
"""Método para receber e registrar uma jogada.
Deve também alternar os jogadores. Não há retorno de valores."""

def limpa_jogadas():
    #Reiniciar os botões, cliques, etc.
    #Podemos fazer um botão pra isso
    verifica_ganhador() = verifica
    
    #Reiniciar registro de jogadas
    matrizX.clear()
    matrizO.clear()
    
    #Reiniciar botões
    
    #Reiniciar jogador
    if verifica == 1:
        self.player = self.player[0]
    elif verifica == 2:
        self.player = self.player[1]
    else:
        sorteia_iniciante()
        
    
"""Método para limpar as jogadas, ou seja, reinicia o jogo (não
limpará a tela – lembre-se que a classe Jogo não tem acesso à classe
Tabuleiro), mantendo a vez do jogador."""
