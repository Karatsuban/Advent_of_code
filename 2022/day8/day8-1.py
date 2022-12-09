with open("input8.txt") as file:
    lines = file.readlines()


# the goal here is to generate a "view" from each side and combine them to the final view
# then, count all the visible trees


def visible_from(side, S):
    x = 0
    y = 0
    b_beg = 0
    b_end = len(S)
    b_step = 1
    a_beg = 0
    a_end = len(S[0])
    a_step = 1
    
    if side == "up":
        y = -1
    if side == "down":
        b_beg, b_end = b_end-1, b_beg-1
        b_step = -1
        y = +1
    if side == "left":
        x = -1
    if side == "right":
        x = +1
        a_beg, a_end = a_end-1, a_beg-1
        a_step = -1
        
    W = [[0 for _ in S] for _ in S[0]]
    H = [[0 for _ in S] for _ in S[0]]

    for b in range(b_beg,b_end,b_step):
        for a in range(a_beg,a_end,a_step):
            if b==0 or b==len(S)-1 or a==0 or a==len(S[0])-1: # on border
                W[b][a] = 1 # tree is visible
                H[b][a] = S[b][a] # max height = cur height
            else:
                if S[b][a] > H[b+y][a+x]: # if the actual tree is taller than all the previous
                    W[b][a] = 1 # visible 
                    H[b][a] = S[b][a] # update max height with the new value
                else:
                    H[b][a] = H[b+y][a+x] # update with the old value
    return W    



S = []

for line in lines:
    line = line.replace("\n", "")
    nl = list(map(int, line))
    zr = [0] * len(nl)
    S.append(nl)
    



c1 = visible_from("up", S)
c2 = visible_from("down", S)
c3 = visible_from("left", S)
c4 = visible_from("right", S)


tot = 0
for a in range(len(S)):
    for b in range(len(S[0])):
        tot += max(c1[a][b],c2[a][b],c3[a][b],c4[a][b])

print(tot)
