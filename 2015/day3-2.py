#coding:utf-8

#made by Karatsuban

def exo(S):
    houses = set()
    santa_turn = True
    Sx = Sy = 0
    Rx = Ry = 0
    houses.add((Sx,Sy))
    houses.add((Rx,Ry))
    for direction in S:
        if direction == "^":
            Sy -= santa_turn
            Ry -= not santa_turn
        elif direction == "v":
            Sy += santa_turn
            Ry += not santa_turn
        elif direction == "<":
            Sx -= santa_turn
            Rx -= not santa_turn
        elif direction ==  ">":
            Sx += santa_turn
            Rx += not santa_turn
        houses.add((Sx,Sy))
        houses.add((Rx,Ry))
        santa_turn = not santa_turn
    return len(houses)


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo(S))
else:
    with open("input3.txt", "r") as file:
        print(exo(file.readlines()[0]))
