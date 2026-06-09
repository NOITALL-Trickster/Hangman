import random

HANGMANPICS = ['''
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

word_list = ['lamp', 'fire', 'king','wakanda']

rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print(chosen_word)

for i in range(len(chosen_word)):
    print(end='_')
print()
# TODO: Keep track of player lives using hangman symbols
correct_letters = []
user_won = False
lives = len(HANGMANPICS)
while not user_won:

    if lives <= 1:
        user_won = True
    else:

        guess = input("Guess a letter: ")
        guess = guess.lower()

        display = ""
        for letter in chosen_word:
            if guess == letter:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += '_'
        if '_' not in display:
            user_won = True

        if guess not in chosen_word:
            lives -= 1
        print(display)
        print(HANGMANPICS[(lives * -1)])

if user_won and lives <= 1:
    print("You Lose!")
