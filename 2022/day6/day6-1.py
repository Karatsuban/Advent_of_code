with open("input6.txt") as file:
    line = file.readlines()[0]
    nb = 0
    while len(set(line[nb:nb+4])) != 4:
        nb+=1

print(nb+4)
