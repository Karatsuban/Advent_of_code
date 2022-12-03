#coding:utf-8

with open("input3.txt") as file:
    tot = 0
    L = []
    for idx, line in enumerate(file.readlines()):

        txt = line.strip()
        L.append(set(txt))

        if (idx+1) %3 == 0:
            common = L[0].intersection(L[1]).intersection(L[2])
            common = list(common)[0]
            if ord("a") <= ord(common) <= ord("z"):
                val = ord(common)-ord("a")+1
            else:
                val = ord(common)-ord("A")+27

            tot += val
            L = []


print(tot)
                

