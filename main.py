import random

word_list = ['lamp', 'fire', 'king','wakanda']

rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print(chosen_word)
# TODO: Create a placeholder for the chosen_word
for i in range(len(chosen_word)):
    print(end='_')
print()

guess = input("Guess a letter: ")
guess = guess.lower()
# TODO: Replace the guess letter with right places in placeholder
for letter in chosen_word:
    if letter == guess:
        print(letter, end='')
    else:
        print('_',end='')
print()
