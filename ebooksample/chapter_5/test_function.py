from __future__ import division

def get_vowel_prop(text, sig_figs=2):
    a_count = text.lower().count('a')
    e_count = text.lower().count('e')
    i_count = text.lower().count('i')
    o_count = text.lower().count('o')
    u_count = text.lower().count('u')
    prop = (a_count + e_count + i_count + o_count + u_count) / len(text)
    return round(prop, sig_figs) 

assert get_vowel_prop('a') == 1
assert get_vowel_prop('b') == 0
assert get_vowel_prop('abab') == 0.5
assert get_vowel_prop('abb') == 0.33
assert get_vowel_prop('abb', 5) == 0.33333 
