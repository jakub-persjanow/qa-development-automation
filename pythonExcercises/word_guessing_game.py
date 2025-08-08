import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

# 1 runda: Guess the word!
# - - - - - -
# user wprowadza jedną literkę np.: p
# p - - - - -
# user wprowadza liretkę np.: w
# wrong letter, remaining guesses: n-1 (n na początku = 12)
# p - - - - -
# user wprowadza liretkę np.: t
# p - t - - -
