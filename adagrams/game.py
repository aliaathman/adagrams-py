import random

letter_pool = [['A'] * 9, ['B'] * 2, ['C'] * 2, ['D'] * 4, ['E'] * 12, ['F'] * 2, ['G'] * 3, ['H'] * 2, ['I'] * 9, 'J', 'K' , ['L'] * 4, 
['M'] * 2, ['N'] * 6, ['O'] * 8, ['P'] * 2, 'Q', ['R'] * 6, ['S'] * 4, ['T'] * 6, ['U'] * 4, ['V'] * 2, ['W'] * 2, 'X', ['Y'] * 2, 'Z']
# Nested list that contains all the letters that a player can draw from

def draw_letters():
    
    flat_pool = [l for letter in letter_pool for l in letter]
    # flattened list from letter_pool
    hand = []

    for i in range(10):
        letter = random.choice(flat_pool) # function that choose random letter from the flattened list 
        hand.append(letter)
        flat_pool.remove(letter) # after appending each letter remove 
    return hand
    
def uses_available_letters(word, letter_bank):

    word_letter_frequency = {}
    letter_bank_frequency = {}

    # need to build a dictionary to count the letters in word and in the letter bank
    # function casefold to check and ignore if cases are different.
    for letter in letter_bank:
        if letter not in letter_bank_frequency:
            letter_bank_frequency[letter] = 1
        else:
            letter_bank_frequency[letter] += 1
    for letter in word.upper():
        if letter not in word_letter_frequency:
            word_letter_frequency[letter] = 1
        else:
            word_letter_frequency[letter] += 1
        

    if all((k in letter_bank_frequency and letter_bank_frequency[k] == v) for k,v in word_letter_frequency.items()):
        return True
    else:
        return False



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass