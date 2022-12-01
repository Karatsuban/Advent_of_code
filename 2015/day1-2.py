#coding:utf-8

#made by Karatsuban

def count(S):
    count = 0
    for a in range(len(S)):
        if S[a] == "(":
            count += 1
        else:
            count -= 1
        if count == -1:
            return a+1
    return -1

S = input("?")
print(count(S))
