# store all the titles, dates and types
title_1 = "The_Mudfog_Papers"
title_2 = "The Old Curiosity Shop"
title_3 = "A Christmas Carol"
date_1 = 1838
date_2 = 1841
date_3 = 1843
type_1 = "short stories"
type_2 = "NOVEL"
type_3 = "novella"

# fix the formatting errors
new_title_1 = title_1.replace('_', ' ')
new_type_2 = type_2.lower()

# open the output file and write the output
csv_output = open("works.csv", "w")
csv_output.write("title, completed, type\n")
csv_output.write(new_title_1 + "," + str(date_1) + "," + type_1 + "\n")
csv_output.write(title_2 + "," + str(date_2) + "," + new_type_2 + "\n")
csv_output.write(title_3 + "," + str(date_3) + "," + type_3 + "\n")
csv_output.close()
