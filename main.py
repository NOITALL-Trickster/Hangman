import random
from hangman_worlist import word_list
from hangman_art import HANGMANPICS

rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print("Welcome to Hangman!")
print()

print("The dashes below represent the number of letters in the words you chose\n")

for i in range(len(chosen_word)):
    print(end='_')
print()


correct_letters = []
user_won = False
right_guess = False
lives = len(HANGMANPICS)

print(f"You Have a total of {lives} lives!")
print()

print("Happy Hangman!")
print()
while not user_won:

    if lives <= 1:
        user_won = True
    else:

        guess = input("Guess a letter: ")
        guess = guess.lower()

        display = ""
        for letter in chosen_word:
            if guess == letter:
                right_guess = True
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += '_'
        if right_guess:
            print(f"The letter '{guess}' is in the word")
            right_guess = False
        else:
            print(f"The letter '{guess}' is not in the word")
        if '_' not in display:
            user_won = True

        if guess not in chosen_word:
            lives -= 1
            print("Number of lives:", lives)
        print(display)
        print(HANGMANPICS[(lives * -1)])

if user_won and lives <= 1:
    print("******************You Lose!********************")
else:
    print("******************You Won!*********************")
