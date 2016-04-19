import numpy as np
import classetabuleiro

class Jogo():
  def __init__(self):
    self.tabuleiro = tabuleiro.classetabuleiro()

  def iniciar(self):
    self.window.mainloop()
    
  def sorteia_iniciante():
    a = random.randint(0,1)
    #Se o clique for 0 o jogador X inicia, caso for 1, o jogador O inicia.
    if a == 0:
        self.player = self.player[0]
    else:
        self.player = self.player[1]
    
  def recebe_jogada(linha, coluna):
    verifica_ganhador() = verifica
    matriz = np.array([None,None,None][None,None,None][None,None,None])
    
    #Registrar jogada
    while True:
        if verifica == -1:
            if matriz[linha][coluna] == None:
                if self.player == 0:
                    self.clicou(linha,coluna)
                    matriz[linha][coluna] = 1
                    self.player = self.player[1]
                elif self.player == 1:
                    self.clicou(linha,coluna)
                    matrizO[linha][coluna] = 0
                    self.player = self.player[0]
        if verifica >= 0:
            break
        
"""Método para receber e registrar uma jogada.
Deve também alternar os jogadores. Não há retorno de valores."""

  def verifica_ganhador():
    #Verificação das possíveis vitórias
    #Verificar quem ganha, -1 indica que o jogo está em andamento
  
    #Colocar sleep e depos limpa_jogadas? ##################################
        print("Deu Velha!")
        return 0
        print("O jogador 1 (X) venceu!")
        return 1
        print("O jogador 2 (O) venceu!")
        return 2
    else:
        return -1
        
def limpa_jogadas():
    #Reiniciar os botões, cliques, etc.
    #Podemos fazer um botão pra isso
    verifica_ganhador() = verifica
    
    #Reiniciar registro de jogadas
    matriz = np.array([None,None,None][None,None,None][None,None,None])
    
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
