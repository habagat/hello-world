from __future__ import division

sen = "Thirty years ago, Marseilles lay burning in the sun, one day."

# extract the city name and calculate the percentage
city_name = sen[18:28]
percentage = 100 * (len(city_name) / len(sen))

print(percentage)
