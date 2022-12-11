with open("input10.txt") as file:
    lines = file.readlines()


cycles = [1] # value to add to X at the end of each cycle
idx = 0
for line in lines:
    cur_cycle = 0
    cmd = line.replace("\n", "").split()
    if cmd[0] == "addx":
        cycles += [0,int(cmd[1])]
    else:
        cycles.append(0)

X = sum([ sum(cycles[:k])*k for k in [20,60,100,140,180,220]])

print(X)
        
