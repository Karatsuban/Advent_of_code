#coding:utf-8

# made by Karatsuban

import itertools

def exo(seq, nb):

    for a in range(nb):
        new_seq = ""
        digit = seq[0]
        count = 0
        for b in seq:
            if b == digit:
                count += 1
            else:
                new_seq += str(count)+digit
                digit = b
                count = 1
        new_seq += str(count)+digit
        seq = new_seq
    return len(seq)


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo(S, 5))
else:
    #with open("input9.txt","r") as file:
    #    print(exo(file.readlines()))
    print(exo("1113222113", 50))
