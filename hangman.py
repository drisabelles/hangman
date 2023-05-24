import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Vamos jogar forca!')
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
        guess = input('Por favor, tente adivinhar a palavra ou uma letra: ').upper()
        print('\n')
        print('----- * ----- * -----')
        print('\n')

        if len(guess) == 1 and guess.isalpha():
            
            if guess in guessed_letters:
                print('Você já palpitou essa letra!')
            
            elif guess not in word:
                print('A palavra não contém a letra', guess)
                tries -= 1
                guessed_letters.append(guess)
            
            else: 
                print('Parabéns! Essa palavra possui', guess)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            
            if guess in guessed_words:
                print('Você já palpitou essa palavra!')
            
            elif guess != word:
                print(guess, 'não é a palavra certa :(')
                tries -= 1
                guessed_words.append(guess)
            
            else:
                guessed = True
                word_completion = word

        else:
            print('Esse palpite não é válido :(')
            print('\n')
            print('----- * ----- * -----')
            print('\n')

        print(display_hangman(tries))
        print(word_completion)
        print('\n')

    if guessed:
        print('Parabéns, você descobriu a palavra!')
        print('\n')
        print('----- * ----- * -----')
        print('\n')

    else: 
        print('Que pena, acabaram as suas tentativas! A palavra era ' + word + '. Quem sabe na próxima vez você consegue!')
        print('\n') 
        print('----- * ----- * -----')
        print('\n')

def display_hangman(tries):
    stages = [  
        # final state: head, torso, both arms, and both legs
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,
        # head, torso, both arms, and one leg
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,
        # head, torso, and both arms
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,

        # head, torso, and one arm
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,

        # head and torso
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,

        # head
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,

        # initial empty state
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input('Que tal jogar novamente? Digite S para sim ou N para não: ').upper() == "S":
        print('\n')
        print('----- * ----- * -----')
        print('\n')
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()