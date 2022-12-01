#coding:utf-8


L = []

with open("input1.txt") as file:
    S = 0
    for line in file.readlines():
        if line != "\n":
            S += int(line.strip())
        else:
            L.append(S)
            S = 0
    L.append(S)

S = 0
for a in range(3):
    val = max(L)
    S += val
    b = L.index(val)
    L.pop(b)

print(S)
