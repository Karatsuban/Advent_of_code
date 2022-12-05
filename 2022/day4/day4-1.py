# does not seem to work. my code and other's (working!) code return the same result, but the answer is not accepted by AoC. An input problem maybe ? Dunno, but I'm pulling my hair off !
with open("input4.txt") as file:
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
