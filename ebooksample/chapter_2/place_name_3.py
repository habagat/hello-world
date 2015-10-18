sen = "Thirty years ago, Marseilles lay burning in the sun, one day."

# split the sentence into before, name and after
before_city_name = sen[0:18]
city_name = sen[18:28]
after_city_name = sen[28:]

# change the name to upper case and concatenate
print(before_city_name + city_name.upper() + after_city_name)
