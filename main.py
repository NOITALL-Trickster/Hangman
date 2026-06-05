import random

word_list = ['lamp', 'fire', 'king']
# TODO: randomly get a word from word_lis and tprint the chosen world
rand = random.randint(0, len(word_list)-1)
chosen_word = word_list[rand]

print(chosen_word)
