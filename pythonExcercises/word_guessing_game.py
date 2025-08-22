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
hiddenWord = ["-"] * len(word) 

user_guessed_characters = []

while "-" in hiddenWord and user_guess < chances:
    print(" ".join(hiddenWord))
    user_input = str(input("Provide a letter "))
    if len(user_input) > 1:
        user_guess +=1
        print('You can only use 1 letter, remaining guesses: ', chances-user_guess)
        continue

    if user_input in user_guessed_characters:
        user_guess +=1
        print('letter already guessed, remaining guesses: ', chances-user_guess)

    if user_input in word:
        user_guessed_characters.append(user_input)
        for i, character in enumerate(word): 
            if character == user_input:
                hiddenWord[i] = user_input

    else:
        user_guess += 1
        print('wrong letter, remaining guesses: ', chances-user_guess)

if "-" not in hiddenWord:
    print("Winner!")
else:
    print("Looser!")
