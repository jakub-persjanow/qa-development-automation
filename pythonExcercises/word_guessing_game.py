import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# 1 runda: Guess the word!
# - - - - - -
# user wprowadza jedną literkę np.: p
# p - - - - -
# user wprowadza liretkę np.: w
# wrong letter, remaining guesses: n-1 (n na początku = 7)
# p - - - - -
# user wprowadza liretkę np.: t
# p - t - - -

word = random.choice(words)
chances = 7
user_guess = 0
hiddenWord = ["-"] * len(word) # początkow próbowałem uzyc replace() ale po pierwsze zamienialo tylko biezacego stringa a reszta pozostawala "-" a po drugie potrzebowalem miec indeksy
print('Guess the word!')

while "-" in hiddenWord and user_guess < chances:
    print(" ".join(hiddenWord))
    user_input = str(input("Provide a letter "))

    if user_input in word:
        for i, character in enumerate(word): #musiałem znaleźć enumerate, brakowało mi metody która daje i element w stringu i jego indeks
            if character == user_input:
                hiddenWord[i] = user_input

    else:
        user_guess += 1
        print('wrong letter, remaining guesses: ', chances-user_guess)

if "-" not in hiddenWord:
    print("Winner!")
else:
    print("Looser!")


# problemy w kodzie:
# mozna wprowadzac kilka razy te samą literę i liczba szans nie spada,
# mozna wprowadzic wiecej niz jedna litere i liczba szans spada
