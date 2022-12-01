#coding:utf-8

# made by Karatsuban

import itertools

def exo(pwd):
    is_bad = True
    while is_bad:
        #is_bad = False
        digit = [ord(k)-ord("a") for k in pwd][::-1]
        digit[0] += 1
        for a in range(len(digit)-1):
            if digit[a] >= 26:
                digit[a] = 0
                digit[a+1] += 1
        digit = digit[::-1]
        pwd = "".join([chr(k+ord("a")) for k in digit])
        #print(pwd)
        
        R1 = rule1(digit)
        R2 = sum([letter in pwd for letter in "iol"]) == 0
        R3 = rule3(pwd)
        #print(R1, R2, R3)
        if R1 & R2 & R3:
            is_bad = False
    
    return pwd

def rule1(S):
    #print("-".join(["S"]+[str(S[k+1]-S[k]) for k in range(len(S)-1)]+["E"]))
    return "-1-1-" in "-".join(["S"]+[str(S[k+1]-S[k]) for k in range(len(S)-1)]+["E"])

def rule3(S):
    idx = []
    pairs = set()
    for a in range(len(S)-1):
        if S[a] == S[a+1]:
            pairs.add(S[a:a+2])
            idx.append(a)
    #print(pairs, idx)
    if len(pairs) < 2:
        return False

    dist = [idx[k+1] - idx[k] for k in range(len(idx)-1)]
    if min(dist) >= 2:
        return True
    return False

test = input("Test ? v/f ")
if not "f" in test.lower():
    S = input("?")
    print(exo(S))
else:
    print(exo("cqjxjnds"))

