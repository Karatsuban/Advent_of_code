with open("input9.txt") as file:
    lines = file.readlines()


def dist(x1,y1,x2,y2):
    return abs(x1-x2),abs(y1-y2)

def off(x1,x2):
    if x1 == x2:
        return 0
    return (x1-x2)/abs(x1-x2)

def new_pos(x1,y1,x2,y2):
    dx,dy = dist(x1,y1,x2,y2)
    x_off = 0
    y_off = 0

    
    if dx+dy == 2:
        if dx != dy: # T and H are not in diagonal
            x_off = off(x1,x2)
            y_off = off(y1,y2)

    if dx+dy > 2:
        x_off = off(x1,x2)
        y_off = off(y1,y2)
    
    return x2+x_off, y2+y_off # don't move

hx = hy = tx = ty = 0


positions = set()

for line in lines:
    line = line.replace("\n", "")
    direction, count = line.split()
    x = y = 0
    if direction == "U":
        y = 1
    elif direction == "D":
        y = -1
    elif direction == "L":
        x = -1
    else:
        x = 1

    for k in range(int(count)):
        hx += x
        hy += y
        tx,ty = new_pos(hx,hy,tx,ty)
        if (tx,ty) not in positions:
            positions.add((tx,ty))

print(len(positions))
