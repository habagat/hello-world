from __future__ import division

def is_vowel_rich(word):
    letters = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for letter in letters:
        letter_count = word.lower().count(letter)
        total = total + letter_count
    proportion = total / len(word)
    if proportion >= 0.5:
        return True
    else:
        return False


print(is_vowel_rich("ignuana"))
print(is_vowel_rich("lizard"))
