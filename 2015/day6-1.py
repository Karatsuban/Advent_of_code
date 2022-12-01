#coding:utf-8

#made by Karatsuban

import numpy as np

def exo(T):
    lights = np.zeros([1000,1000])
    count = 0
    
    for word in T:
        word = word.replace("\n","").split()[-4:]
        
        command = word[0]
        coords = [int(k) for k in (word[1]+","+word[3]).split(",")]
        

        for y in range(coords[1], coords[3]+1):
            for x in range(coords[0], coords[2]+1):
                if command == "on":
                    lights[x,y] = 1
                elif command == "off":
                    lights[x,y] = 0
                elif command == "toggle":
                    lights[x,y] = 1-lights[x,y]
        

    count = sum(sum(lights))
    return count


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo([S]))
else:
    with open("input6.txt","r") as file:
        print(exo(file.readlines()))
