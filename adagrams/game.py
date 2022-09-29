import random
from typing import Counter
letter_bank = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    
    letter_pool = [key for key, val in letter_bank.items() for i in range(val)]
    last_index = len(letter_pool) - 1
    hand = []
    
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        letter_pool[last_index], letter_pool[rand_index] = letter_pool[rand_index], letter_pool[last_index]
        last_index -= 1
        
    for i in range(10):
        hand.append(letter_pool[i])
    return hand
def uses_available_letters(word, letter_bank):

    word_letter_frequency = Counter(word.upper())
    letter_bank_frequency = Counter(letter_bank)

<<<<<<< HEAD
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
        
    if all((word in letter_bank_frequency and letter_bank_frequency[word] == score) for word,score in word_letter_frequency.items()):
=======
    if all((k in letter_bank_frequency and letter_bank_frequency[k] == v) for k,v in word_letter_frequency.items()):
>>>>>>> ec58fc64940518fd7c8b1e629c934dacb34df35a
        return True
    return False

def score_word(word):

    score_chart = {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ'
    }
    score = 0
    if len(word) > 6:
        score += 8
    score += sum([points for points, letters in score_chart.items() for char in word if char.upper() in letters])
    return score

def get_highest_word_score(word_list):

    words_score_dict = {}
    for word in word_list:
        score = score_word(word)
        words_score_dict[word] = score
    highest_score = max(words_score_dict.values())

    for word,score in words_score_dict.items():
        if len(word) == 10 and score == highest_score:
            return word, highest_score
    return max(words_score_dict.items()) 



