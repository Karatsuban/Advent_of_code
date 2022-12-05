import re

L_stacks = [[] for _ in range(9)]

with open("input5.txt") as file:
    content = file.readlines()
    for line in content[:8]:
        line = line.replace("\n", "")
        disp = re.sub("    ", " [#]", line)
        disp = re.sub("(\[|\])", "", disp)
        vals = disp.split()
        
        for idx, a in enumerate(vals):
            if a != "#":
                L_stacks[idx].insert(0,a)
        

    for line in content[10:]:
        cmd = line.split()
        nb, orig, dest = int(cmd[1]), int(cmd[3])-1, int(cmd[5])-1
        temp = []
        for a in range(nb):
            temp.insert(0, L_stacks[orig].pop(-1))
        L_stacks[dest] += temp

for a in range(len(L_stacks)):
    print(L_stacks[a][-1], end="")
