from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
    '''
        +-------+
        |
        |
        |
        |
        |
    ==============
    ''',
    '''
        +-------+
        |       |
        |       O
        |
        |
        |
    ===============
    ''',
    '''
        +-------+
        |       |
        |       O
        |       |
        |
        |
    ===============
    ''',
    '''
        +-------+
        |       O
        |      -|
        |
        |
        |
    ===============
    ''',
    '''
        +-------+
        |       |
        |       O
        |      -|-
        |
        |
    ===============
    ''',
    '''
        +-------+
        |       |
        |       O
        |      -|-
        |      /
        |
    ===============
    ''',
    '''
        +-------+
        |       |
        |       O
        |      -|-
        |      / /
        |
    ===============
    '''
]
    print(graphic[hangman])
    return

def start():
    print("Vamos jogar Jogo da Forca?")
    while game():
        pass
    scores()


def game():
    dictionary = ['gnu', 'kernel', 'linux', 'mageia', 'penguin', 'ubuntu']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ''
    # guesses = 0
    # letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and (''.join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("Você já escolheu", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print(f"Desculpe, {letter}, não é o que estamos procurando.")
                else:
                    print(f"Parabéns, {letter} está correto.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Escolha outro.")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Suposição: ", letters_tried)

        if letters_wrong == tries:
            print("Fim de jogo!")
            print("A palavra era", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print("Você ganhou!")
            print("A palavra era ", word)
            player_score += 1
            break
    return play_again()

def guess_letter():
    print()
    letter = input("Qual letra você escolhe: ")
    letter.strip()
    letter.lower()
    print()
    return letter

def play_again():
    answer = input("Gostaria de jogar novamente? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Sim", "s", "S"):
        return answer
    else:
        print("Obrigado por jogar nosso jogo. Vejo você na próxima vez!")

def scores():
    global player_score, computer_score
    print("MAIORES SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == '__main__':
    start()
