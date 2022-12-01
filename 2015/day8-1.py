#coding:utf-8

#made by Karatsuban

import ast

def exo3(T):
    diff = 0
    for a in T:
        a = a.replace("\n","")
        b = ast.literal_eval(a)

        diff += len(a)-len(b)
    return diff



test = input("Test ? v/f ")
if "v" in test.lower():
    #S = input("?")
    #print(exo([S]))
    S = ['"aaa\"aaa"']
    print(exo3(S))
else:
    with open("input8.txt","r") as file:
        print(exo3(file.readlines()))


