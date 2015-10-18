from __future__ import division

def get_vowel_prop(text, sig_figs=2):
    a_count = text.lower().count('a')
    e_count = text.lower().count('e')
    i_count = text.lower().count('i')
    o_count = text.lower().count('o')
    u_count = text.lower().count('u')
    prop = (a_count + e_count + i_count + o_count + u_count) / len(text)
    return round(prop, sig_figs) 


data = open("data.csv") 
 
for line in data: 
    
    # split the line up 
    columns = line.rstrip("\n").split(",") 
 
    # assign the columns to variables 
    title = columns[0] 
    year = int(columns[1]) 
    type = columns[2] 
    length = int(columns[3]) 
 
 
    if get_vowel_prop(title) >= 0.3 and length < 300000: 
        print(title)
