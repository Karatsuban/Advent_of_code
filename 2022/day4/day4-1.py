"""with open("input4.txt") as file:
    nb = 0
    for line in file.readlines():
        v1, v2 = line.strip().split(",")
        v1 = v1.split("-")
        v2 = v2.split("-")
        a,b = list(map(int, v1))
        c,d = list(map(int, v2))

        if a <= c <= d <= b or c <= a <= b <=d:
            nb += 1

print(nb)
"""

with open("input4.txt") as f:
    lines = [[[int(i) for i in k.split("-")] for k in x.split(",")] for x in f]

print(sum(a <= c <= d <= b or c <= a <= b <= d for (a,b), (c,d) in lines))
print(sum(any([a <= c <= b, a <= d <= b, c <= a <= d, c <= b <= d]) for (a,b), (c,d) in lines))

# Alternative for Part 2
print(sum([max(a,c) <= min(b,d) for (a,b), (c,d) in lines]))
