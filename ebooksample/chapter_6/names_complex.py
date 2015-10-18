names = ["Pip", "Joe", "Magwitch", "Matthew", "Estella"]
for name in names:
    if (name.startswith('M') or name.startswith('J')) and len(name)>=4:
        print(name)
