text = "Night is generally my time for walking. In the summer I often leave home early in the morning, and roam about fields and lanes all day, or even escape for days or weeks together; but, saving in the country, I seldom go out until after dark, though, Heaven be thanked, I love its light and feel the cheerfulness it sheds upon the earth, as much as any creature living."

period_position = text.find(".")
first_length = period_position + 1
second_length = len(text) - first_length

print("First sentence is " + str(first_length) + " characters long")
print("Second sentence is " + str(second_length) + " characters long")
