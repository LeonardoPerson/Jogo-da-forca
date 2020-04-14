# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
	|
	|
	|
	|
=========''', '''

+---+
|   |
O   |
	|
	|
	|
=========''', '''

+---+
|   |
O   |
|   |
	|
	|
=========''', '''

 +---+
 |   |
 O   |
/|   |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
	 |
	 |
=========''', '''            

 +---+
 |   |
 O   |
/|\  |
/    |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
	 |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word

    # ---------------------------------------------------------------------------------------------------------------
    # Método para adivinhar a letra, retornando verdadeiro para letra errada, e falso para letra correta
    def guess(self, letter):
        self.letter = letter
        # A lista abaixo sempre será vazia quando esse método for chamado após a digitação da letra
        self.existe = list()
        for indice, valor in enumerate(self.word):
            if self.letter == valor:
                self.existe.append({indice: valor})
        # A lista não é abastecida em caso de letra errada
        if len(self.existe) == 0:
            self.letraErrada += "\n" + self.digitacao
            return True
        # A lista é abastecida em caso de letra certa
        else:
            for item in self.existe:
                self.indice = list(item.keys())
                self.valor = list(item.values())
                self.desoculta[self.indice[0]] = self.valor[0]
            self.letraCerta += "\n" + self.valor[0]
            return False

    # ---------------------------------------------------------------------------------------------------------------
    # Método para verificar se o jogo terminou
    def hangman_over(self):
        self.verificaTermino = ""
        for item in self.desoculta:
            self.verificaTermino += item
        if self.verificaTermino != self.desoculta and self.contador == 6:
            return True

    # ----------------------------------------------------------------------------------------------------------------
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        self.verificaJogador = ""
        self.resultado = False
        for item in self.desoculta:
            self.verificaJogador += item
        if self.verificaJogador == self.word:
            self.resultado = True
            return self.resultado

    # ---------------------------------------------------------------------------------------------------------------
    # Método para não mostrar a letra no board
    def hide_word(self):
        self.oculta = list(map(lambda x: "_", self.word))
        return self.oculta

    # ----------------------------------------------------------------------------------------------------------------
    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        self.letraErrada = ""
        self.letraCerta = ""
        self.desoculta = Hangman.hide_word(self)
        self.contador = 0
        while self.contador <= 6:
            print(board[self.contador])
            print("\nPalavra: " + " ".join(self.desoculta))
            print("\nLetras erradas: %s" % (str(self.letraErrada)))
            print("\nLetras corretas: %s" % (str(self.letraCerta)))
            if Hangman.hangman_won(self):
                break
            if Hangman.hangman_over(self):
                break
            self.digitacao = input("\nDigite uma letra: ")
            # Se a letra não for repetida ou vazia, o método guess() irá tratar a letra
            if self.digitacao not in self.desoculta and self.digitacao != "":
                if self.digitacao not in self.letraErrada:
                    self.resultado = Hangman.guess(self, letter=self.digitacao)
                    # True será retornodo se a letra for errada para incrementar o board
                    if self.resultado:
                        self.contador += 1
            # Para letra repetida, não há incrementação do board
            else:
                print("Letra repetida ou entrada vazia!")


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você!\n')


# Executa o programa
if __name__ == "__main__":
    main()
