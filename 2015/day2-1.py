#coding:utf-8

#made by Karatsuban

def count(S):
    total = 0
    for a in S:
        dims = [int(k) for k in a.split("x")]
        l,w,h = dims
        areas = [l*w, w*h, h*l]
        slack = min(areas)
        surface = 2*sum(areas)
        total += (surface + slack)
    return total

with open("input2.txt", "r") as file:
    print(count(file.readlines()))
    
