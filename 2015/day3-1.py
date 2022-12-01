#coding:utf-8

#made by Karatsuban

def exo(S):

    houses = set()
    x = y = 0
    houses.add((x,y))
    for direction in S[0]:
        if direction == "^":
            y -= 1
        elif direction == "v":
            y += 1
        elif direction == "<":
            x -= 1
        elif direction ==  ">":
            x += 1
        houses.add((x,y))
    return len(houses)


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo(S))
else:
    with open("input3.txt", "r") as file:
        print(exo(file.readlines()))
