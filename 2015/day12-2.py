#coding:utf-8

# made by Karatsuban


# to try 96852

def exo(J, term):

    to_cut = []
    J += " "*len(term)

    S_rep, L_idx, term_rep_idx = do_rep(J, term)
    
    #print(term_rep_idx)
    for b in range(len(term_rep_idx)):  # a takes all the places of term in the representation string
        a = term_rep_idx[b]
        #print(b,a)
        idx_opener = first_open(S_rep, a)  # first opener before the idx a
        idx_closer = last_close(S_rep, a)
        if S_rep[idx_opener] == "{" and S_rep[idx_closer] == "}":  # the term is between {}
            real_open = L_idx[idx_opener]
            real_clos = L_idx[idx_closer]
            to_cut = [[real_open, real_clos+1]] + to_cut

    for a,b in to_cut:
        J = J[:a]+(b-a)*" "+J[b:]
                
    with open("shiet.txt", "w") as file:
        file.write(J)
    return count_digit(J)


def do_rep(J, term):
    S_rep = ""
    L_idx = []
    term_rep_idx = []
    for a in range(len(J)):
        if J[a] in "[]{}":
            S_rep += J[a]
            L_idx.append(a)
        if J[a:a+len(term)] == term:
            term_rep_idx.append(len(S_rep)) # idx of the term in the representation string
            S_rep += "#"
            L_idx.append(a)
    return S_rep, L_idx, term_rep_idx


def first_open(L, idx):
    # find the id of the first opener before idx in L (ie { or [ )
    opening = 0
    closing = 0
    while True:
        idx -= 1
        if idx < 0:
            break
        if L[idx] in "[{":
            opening += 1
        if L[idx] in "]}":
            closing += 1
        if opening > closing:
            break
    return idx

def last_close(L, idx):
    # find the id of the first closer before idx in L (ie } or ] )
    opening = 0
    closing = 0
    while True:
        idx += 1
        if idx > len(L):
            break
        if L[idx] in "[{":
            opening += 1
        if L[idx] in "]}":
            closing += 1
        if closing > opening:
            break
    return idx
    



def count_digit(J):
    S = ""
    somme = 0
    in_digit = False
    for a in J:
        if a in "-0123456789":
            in_digit = True
            S += a
        else:
            if in_digit:
                in_digit = False
                somme += int(S)
                S = ""
    return somme


test = input("Test ? v/f ")
if not "f" in test.lower():
    S = input("?")
    print(exo(S,'red'))
else:
    with open("input12.txt", "r") as file:
        print(exo(file.readlines()[0], 'red'))


