#coding:utf-8

#made by Karatsuban

def count(S):
    total = 0
    for a in S:
        dims = [int(k) for k in a.split("x")]
        l,w,h = dims
        min_perim = 2*(sum(dims) - max(dims))
        bow = l*w*h
        total += (min_perim + bow)
    return total


with open("input2.txt", "r") as file:
    print(count(file.readlines()))
