with open("input10.txt") as file:
    lines = file.readlines()


cycles = [] # value to add to X at the end of each cycle
idx = 0
for line in lines:
    cur_cycle = 0
    cmd = line.replace("\n", "").split()
    if cmd[0] == "addx":
        cycles += [0,int(cmd[1])]
    else:
        cycles.append(0)

screen = ""
sprite_x = 1
for idx,pos in enumerate(cycles):
    if sprite_x-1 <= idx%40 <= sprite_x+1:
        screen += "#"
    else:
        screen += "."
        
    sprite_x += pos


for k in range(6):
    print(screen[k*40:(k+1)*40])     
