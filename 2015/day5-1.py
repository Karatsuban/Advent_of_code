#coding:utf-8

#made by Karatsuban


def exo(T):
    count = 0
    dis = ["ab", "cd", "pq", "xy"]
    vow = ["a", "e", "i", "o", "u"]
    doubles = [2*chr(k) for k in range(ord("a"), ord("z")+1)]
    for word in T:
        word = word.replace("\n","")
        #print(word, end=" ")
        is_in = True
        rule1 = sum([word.count(k) for k in vow])
        rule2 = sum([k in word for k in doubles])
        rule3 = sum([k in word for k in dis])
        if rule1 >= 3 and rule2 >= 1 and rule3 == 0:
            count += 1
        # print(rule1, rule2, rule3)
    return count


test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo([S]))
else:
    with open("input5.txt","r") as file:
        print(exo(file.readlines()))
