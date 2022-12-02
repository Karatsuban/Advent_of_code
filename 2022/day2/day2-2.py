#coding:utf-8

new_action = {"A":{"X":"Z", "Y":"X", "Z":"Y"},
           "B":{"X":"X", "Y":"Y", "Z":"Z"},
           "C":{"X":"Y", "Y":"Z", "Z":"X"}}

values = {"X":1, "Y":2, "Z":3}

outcome = {"A":{"X":3, "Y":6, "Z":0},
           "B":{"X":0, "Y":3, "Z":6},
           "C":{"X":6, "Y":0, "Z":3}}


with open("input2.txt") as file:
    score = 0
    for line in file.readlines():
        e1, e2 = line.strip().split()
        e2_p = new_action[e1][e2]
        score += outcome[e1][e2_p]
        score += values[e2_p]

print(score)
