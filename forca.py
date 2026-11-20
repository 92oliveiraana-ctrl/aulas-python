import random

words = ["cão", "gato", "zebra", "pato", "leão", "elefante", "girafa", "raposa", "baleia", "golfinho", "peixe", "lobo", "avestruz", "foca", "doninha", "hiena"]

word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Bem vindo ao jogo da Forca!")
print("Pista: Adivinha o animal.")

while wrong_guesses < max_attempts:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)

    if "_" not in display:
        print("Parabéns! Ganhaste!")
        print("O animal é:", word)
        break

    guess = input("Diz uma letra: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Diz uma letra.")
        continue

    if guess in guessed:
        print("Já adivinhaste essa letra.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Acertaste!")
    else:
        wrong_guesses += 1
        print("Errado!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("O animal era:", word)
    