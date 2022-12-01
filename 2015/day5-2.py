#coding:utf-8

#made by Karatsuban


def exo(T):
    count = 0
    
    for word in T:
        word = word.replace("\n","")
        rule1 = rule2 = False

        
        for k in range(0, len(word)-2):
            if word[k:k+2] in word[k+2:]:
                rule1 = True
                break

        for k in range(0, len(word)-2):
            if word[k] == word[k+2]:
                rule2 = True
                break
        
        if rule1 and rule2:
            count += 1
    return count

test = input("Test ? v/f ")
if "v" in test.lower():
    S = input("?")
    print(exo([S]))
else:
    with open("input5.txt","r") as file:
        print(exo(file.readlines()))
