from __future__ import division

def build_word_freq_dict(text): 
    text = text.lower() 
    for punctuation in [',', ':', '.','"', '!', '?', '--','(', ')', 
                        '\n', '\r']: 
        text = text.replace(punctuation, ' ')
    all_words = text.split(" ") 
 
    word_count = {} 
    for word in all_words: 
        current_count = word_count.get(word, 0) 
        new_count = current_count + 1 
        word_count[word] = new_count 
 
    word_frequency = {} 
    for word, count in word_count.items(): 
        freq = (count / len(all_words)) * 1000000 
        word_frequency[word] = freq 
 
    return word_frequency 
 
# build the frequency dict for Great Expectations
ge_text = open("great_expectations_complete.txt").read() 
ge_word_freqs = build_word_freq_dict(ge_text) 
 
# build the frequency dict for David Copperfield
dc_text = open("david_copperfield_complete.txt").read() 
dc_word_freqs = build_word_freq_dict(dc_text) 
 
# iterate over words in Great Expectations and print them
for word, ge_freq in ge_word_freqs.items(): 
    dc_freq = dc_word_freqs.get(word, 1) 
    if ge_freq > dc_freq * 50: 
        print(word)
