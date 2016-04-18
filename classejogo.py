class Jogo(Tabuleiro):
  def __init__:
      self.clique = 0

  def iniciar(self):
    self.window.mainloop()
    
  def apertou(self):
    self.button.configure(text="O")
    self.button.configure(font="Calibri 100 bold")
    
  def sorteia_iniciante():
    a = random.randint(0,1)
    if a == 0:
        self.clique = 0
    else:
        self.clique = 1
    return a
    
  def verifica_ganhador():
    vitoria = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    if not listaX in vitoria and not listaO in vitoria or len(listaX) = 5 or len(listaO):
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
    
    #Registrar jogada
    
    
    while True:
        if verifica == -1:
            if clique == 0:
                """mudar botao para X"""
                listaX.append()
                sorted(listaX, key=int)
            elif clique == 1:
                """mudar botao para O"""
                listaO.append()
                sorted(listaO, key=int)
        if verifica >= 0:
            break
        
"""Método para receber e registrar uma jogada.
Deve também alternar os jogadores. Não há retorno de valores."""

def limpa_jogadas():
    #Reiniciar os botões, cliques, etc.
    #Podemos fazer um botão pra isso
"""Método para limpar as jogadas, ou seja, reinicia o jogo (não
limpará a tela – lembre-se que a classe Jogo não tem acesso à classe
Tabuleiro), mantendo a vez do jogador."""
