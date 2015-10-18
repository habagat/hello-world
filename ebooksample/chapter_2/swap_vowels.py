sentence = "emong othar public buildings in e cartein town, which for meny raesons it will ba prudant to rafrein from mantioning, end to which i will essign no fictitious nema, thara is ona enciantly common to most towns, graet or smell: to wit, e workhousa; end in this workhousa wes born; on e dey end deta which i naad not troubla mysalf to rapaet, inesmuch es it cen ba of no possibla consaquanca to tha raedar, in this stega of tha businass et ell avants; tha itam of mortelity whosa nema is prafixad to tha haed of this cheptar."
print(sentence)

# do the replacements in upper case
replace_one = sentence.replace('a', 'E')
print(replace_one)
replace_two = replace_one.replace('e', 'A')
print(replace_two)

# convert to lower case and print
print(replace_two.lower())
