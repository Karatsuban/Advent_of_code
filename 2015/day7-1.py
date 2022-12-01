#coding:utf-8

#made by Karatsuban

import numpy as np

def exo(T, end):
    op_names = ['->', 'AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']
    op = {"->":"=", "AND":"&", "OR":"|", "LSHIFT":"<<", "RSHIFT":">>", "NOT":"~"}

    values = {}
    computed = {}
    to_compute = []

    # creates the dict of (key:circuit_name, val:(circuit_logic, dependencies))
    for line in T:
        dep = []
        line = line.replace("\n","").split()
        for idx in range(len(line) - 1):
            elt = line[idx]
            if elt in op_names:  # op change
                line[idx] = op[elt]
            elif not elt.isnumeric():  # elt is a var
                dep.append(elt)  # add circuit name to dependencies list
        to_compute.append([line[-1], "".join(line[:-2]), dep])
    print("HERE", to_compute)
    while to_compute != []:
        name,circuit,dep = to_compute.pop(0)
        new_dep = []
        #print(name, circuit, dep)
        for d in dep:
            if d in values: # if the dependency has already been computed
                circuit = circuit.replace(d, str(values[d])) # replace it in the circuit logic
                #print("\t", circuit)
            else:
                new_dep.append(d)
        if new_dep == []: #all dependencies already computed
            comp_value = eval(circuit)
            if comp_value < 0:  # check overflow
                comp_value = 2**16 + comp_value
            #print("\t\t", circuit, "=", comp_value)
            values[name] = comp_value  # add the eval-ed circuit in values
        else:
            to_compute.append([name, circuit, new_dep])

    print(values)
    print(end, "=", values[end])
    return values[end]

"""
# DOES NOT WORK AS INTENDED
def exo(O, A, end): # ordered_circuits, all_circuits, end_circuit
    values = {}
    for name in O:
        print(name, end="")
        exp, dep = A[name]
        for d in dep:
            exp = exp.replace(d, str(values[d]))  # replace var by its value
        
        comp_value = eval(exp)
        if comp_value < 0:  # check overflow
            comp_value = 2**16 + comp_value
        values[name] = comp_value
        print(values[name])
    print(values)

    return values[end]

def order_in_need_order(T, end):
    # takes T : a circuit (list of operations)
    #     end : the name of last first circuit to be computed
    # order the circuit so as to the last circuit is computed last
    # and all of is its dependencies computed before
    op_names = ['->', 'AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']
    op = {"->":"=", "AND":"&", "OR":"|", "LSHIFT":"<<", "RSHIFT":">>", "NOT":"~"}
    all_circuits = {}
    ordered_circuits = []
    already_computed = set(end)
    dependencies_to_compute = [end]
    
    # creates the dict of (key:circuit_name, val:(circuit_logic, dependencies))
    for line in T:
        dep = []
        line = line.replace("\n","").split()
        for idx in range(len(line) - 1):
            elt = line[idx]
            if elt in op_names:  # op change
                line[idx] = op[elt]
            elif not elt.isnumeric():  # elt is a var
                dep.append(elt)  # add circuit name to dependencies list
        all_circuits[line[-1]] = ("".join(line[:-2]), dep)

    # compute all dependencies until there is no more
    while dependencies_to_compute != []:
        circuit_name = dependencies_to_compute.pop(0) # get the first dep
        for dep in all_circuits[circuit_name][1]: # for each dep of the circuit
            print(dep)
            if dep not in already_computed:
                dependencies_to_compute = [dep] + dependencies_to_compute  # add the dep of this circuit before the other
                already_computed.add(dep)  # it is computed now
            else:
                ordered_circuits.remove(dep) # if already found, we must compute it later (i.e. sooner)
        ordered_circuits.append(circuit_name)
    print("HERE", ordered_circuits)


    return exo(ordered_circuits[::-1], all_circuits, end)
"""

test = input("Test ? v/f ")
if "v" in test.lower():
    #S = input("?")
    S = ["123 -> x",
"456 -> y",
"x AND y -> d",
"x OR y -> e",
"x LSHIFT 2 -> f",
"y RSHIFT 2 -> g",
"NOT x -> h",
"NOT y -> i"]
    print(exo(S, "i"))
else:
    with open("input7.txt","r") as file:
        print(exo(file.readlines(), "a"))
