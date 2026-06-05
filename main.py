import random

word_list = ['lamp', 'fire', 'king','wakanda']

rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print(chosen_word)

for i in range(len(chosen_word)):
    print(end='_')
print()
# TODO: Create a while loop for the user to guess again
display = ""
user_won = False
while not user_won:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    # TODO: Replace the guess letter with right places in placeholder
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
