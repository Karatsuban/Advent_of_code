#coding:utf-8

# found here
# https://blog.jverkamp.com/2015/12/08/advent-of-code-day-8/
# in need of explanation...
# why this does not work ??

import re


"""
def exo(T):
    diff = 0
    for a in T:
        a = a.replace("\n","")
        b1 = re.sub(r'\\', r'\\', a)
        #print([b1])
        b = re.sub(r'"', r'\\\"', a)
        #print([b])

        diff += len(b)-len(a) + 2
    return diff
"""




def exo2(T):
    diff = 0
    for a in T:
        a = a.replace("\n","")
        b = re.sub(r'(["\\])', r'\\\\', a)

        diff += len(b)-len(a)+2
    return diff


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo2([S]))
else:
    with open("input8.txt","r") as file:
        print(exo2(file.readlines()))


