file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
names = ["Pip", "Joe", "Magwitch", "Matthew", "Estella"]
for name in names:
    if name.startswith('M'):
        file1.write(name + "\n")
    else:
        file2.write(name + "\n")
