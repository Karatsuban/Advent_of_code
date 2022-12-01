#coding:utf-8

#made by Karatsuban

import hashlib

def exo(V):
    count = 0
    md_hash = hashlib.md5(V.encode("utf-8")).hexdigest()
    while md_hash[:6] != "000000":
        count += 1
        md_hash = hashlib.md5((V+str(count)).encode("utf-8")).hexdigest()
        if count % 10000 == 0:
            print(count)
    return count


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo(S))
else:
    print(exo("yzbqklnj"))
