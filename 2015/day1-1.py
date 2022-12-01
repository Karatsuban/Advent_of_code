#coding:utf-8

#made by Karatsuban

def count(S):
    up = S.count("(")
    down = S.count(")")
    return up-down

S = input("?")
print(count(S))
