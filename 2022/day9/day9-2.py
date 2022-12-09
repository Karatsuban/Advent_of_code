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


rope = [(0,0) for _ in range(10)]


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

    for _ in range(int(count)):
        hx,hy = rope[0]
        rope[0] = (hx+x, hy+y)
        for k in range(1,10):
            tx, ty = new_pos(*rope[k-1],*rope[k])
            rope[k] = tx,ty
        if rope[-1] not in positions:
            positions.add(rope[-1])

print(len(positions))
