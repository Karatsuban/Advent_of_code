#coding:utf-8

# made by Karatsuban


def exo(J):
    S = ""
    somme = 0
    in_digit = False
    for a in J:
        if a in "-0123456789":
            in_digit = True
            S += a
        else:
            if in_digit:
                in_digit = False
                somme += int(S)
                S = ""
    return somme


test = input("Test ? v/f ")
if not "f" in test.lower():
    S = input("?")
    print(exo(S))
else:
    with open("input12.txt", "r") as file:
        print(exo(file.readline()))

