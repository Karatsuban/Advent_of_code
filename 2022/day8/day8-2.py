with open("input8.txt") as file:
    lines = file.readlines()


def view(L, cur_h):
    """L is the height list of all the tree visible in a certain direction from the tree
    cur_h is the height of the current tree"""
    for idx, x in enumerate(L):
        if x >= cur_h:
            return idx+1
    return len(L)


def view_count(S, x, y):
    """return the view count in each direction"""

    h = S[y][x]
    r = view([S[y][k] for k in range(x+1,len(S[0]))],h)
    l = view([S[y][k] for k in range(x-1,-1,-1)],h)
    u = view([S[k][x] for k in range(y-1,-1,-1)],h)
    d = view([S[k][x] for k in range(y+1, len(S))],h)

    return r*l*u*d


S = []

for line in lines:
    line = line.replace("\n", "")
    nl = list(map(int, line))
    zr = [0] * len(nl)
    S.append(nl)
    

maxi = 0

for b in range(len(S)):
    for a in range(len(S[0])):
        v = view_count(S, a, b)
        if v > maxi:
            maxi = v

print(maxi)
        

