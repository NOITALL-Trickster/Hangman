import random

word_list = ['lamp', 'fire', 'king','wakanda']

rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print(chosen_word)

for i in range(len(chosen_word)):
    print(end='_')
print()
# TODO: Create a while loop for the user to guess again
correct_letters = []
user_won = False
while not user_won:
    guess = input("Guess a letter: ")
    guess = guess.lower()
# TODO: Replace the guess letter with right places in placeholder
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
    print(display)
