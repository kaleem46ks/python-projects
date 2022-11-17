import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)      # randomly choses something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

word = get_valid_word(words)
print(word)
print(set(word))
print(tuple(word))

alphabet = set(string.ascii_uppercase)
print(alphabet)
used_letters = set()
print(alphabet - used_letters)

wrd = 'seed'
print(tuple(wrd))