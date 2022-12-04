import itertools as it

MAT = [[0 for _ in range(8)] for _ in range(8)]

with open("input13.txt") as file:
    persons = dict()
    persons_nb = 0
    for line in file.readlines():
        l = line.strip().split()
        name1, sign, weight, name2 = l[0], l[2], int(l[3]), l[-1][0:-1]

        if name1 not in persons:
            persons[name1] = persons_nb
            persons_nb += 1

        if name2 not in persons:
            persons[name2] = persons_nb
            persons_nb += 1
            
        if sign == "lose":
            weight = -weight

        MAT[persons[name1]][persons[name2]] = weight




def eval_(path):
    indexes = [int(k) for k in path]
    old = indexes[-1]
    tot = 0
    for idx in indexes:
        val1 = MAT[old][idx]
        val2 = MAT[idx][old]
        #print("val for {}->{} = {},{} (tot = {})".format(old, idx, val1, val2, tot))
        tot += val1+val2
        old=idx
        
    return tot


ALL = it.permutations("".join([str(k) for k in range(persons_nb)]), persons_nb)
#print(list(ALL))
maxi = 0
for a in list(ALL):
    val = eval_("".join(a))
    if val > maxi:
         maxi = val

print(maxi)
