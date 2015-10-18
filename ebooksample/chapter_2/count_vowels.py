from __future__ import division

sentence = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

low_sentence = sentence.lower()
length = len(sentence)

# make counts for all the vowels
a_count = low_sentence.count('a')
e_count = low_sentence.count('e')
i_count = low_sentence.count('i')
o_count = low_sentence.count('o')
u_count = low_sentence.count('u')

# use the counts to calculate the proportion
proportion = (a_count + e_count + i_count + o_count + u_count) / length
print("proportion of vowels is " + str(proportion))
