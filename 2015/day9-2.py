#coding:utf-8

# made by Karatsuban

import itertools

def exo(T):
    list_cities = set()
    list_cities_dist = {}
    for a in T:
        a = a.strip()
        c1, _, c2, _, dist = a.split()
        list_cities.add(c1)
        list_cities.add(c2)
        list_cities_dist[c1+c2] = int(dist)
        list_cities_dist[c2+c1] = int(dist)
    
    list_cities = list(list_cities)
    comb = list(itertools.permutations(list_cities, len(list_cities)))

    maxi = 0
    for a in comb:
        long = eval_len(a, list_cities_dist)
        if long > maxi:
            maxi = long
    return maxi

def eval_len(L, list_cities_dist):
    long = 0
    for a in range(0,len(L)-1):
        long += list_cities_dist[L[a]+L[a+1]]
    return long

test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo([S]))
else:
    with open("input9.txt","r") as file:
        print(exo(file.readlines()))


