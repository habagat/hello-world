file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")

names = ["Pip", "Joe", "Magwitch", "Matthew", "Estella"]
for name in names:
    if name.startswith('M'):
        file1.write(name + "\n")
    elif name.startswith('E'):
        file2.write(name + "\n")
    else:
        file3.write(name + "\n")
