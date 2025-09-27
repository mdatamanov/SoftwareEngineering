counter = 0
while counter != 10:
    string = 'hello'
    values = [0, 2, 4, 6, 8, 10]
    memory = ' world'
    if counter in values:
        string = string + ' world'
    print(string)
    counter += 1
if (counter > 7):
    print(string + memory)