from __future__ import division

def get_letter_prop(text, letters=['a', 'e', 'i', 'o', 'u']):
    total = 0
    for letter in letters:
        # convert to lower case and count the letter
        letter_count = text.lower().count(letter.lower())
        # update the total count
        total = total + letter_count

    # calculate the proportion, round it, and return it
    proportion = total / len(text)
    return round(proportion, 2)


assert get_letter_prop('Great Expectations', ['e']) == 0.17
assert get_letter_prop('Great Expectations', ['e', 't']) == 0.33
assert get_letter_prop("Great Expectations", ['G', 'N']) == 0.11
assert get_letter_prop("Great Expectations") == 0.39
