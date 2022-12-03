#coding:utf-8

with open("input3.txt") as file:
    tot = 0
    for line in file.readlines():
        txt = line.strip()
        l = len(txt)
        c1, c2 = set(txt[:l//2]), set(txt[l//2:])
        common = list(c1.intersection(c2))[0]
        if ord("a") <= ord(common) <= ord("z"):
            val = ord(common)-ord("a")+1
        else:
            val = ord(common)-ord("A")+27
        print(common, val)
        tot += val
print(tot)
                

