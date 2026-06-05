import random

word_list = ['lamp', 'fire', 'king']
# TODO: randomly get a word from word_lis and tprint the chosen world
rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print(chosen_word)
# TODO: Ask the user to guess a letter and assign their answer to a variable. Make it lower case
guess = input("Guess a letter: ")
guess = guess.lower()
# TODO: Check if the letter user guessed is actually one of the right letters in chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")