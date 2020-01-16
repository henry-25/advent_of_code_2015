import pprint

tupperware = []


with open('input.txt') as file:
    for line in file:
        tupperware.append(int(line.strip()))


# Part 1
def tup_combinations(available_tup, space):
    tmp_tup = available_tup[:]
    if space == 150:
        return 1
    elif space > 150:
        return 0
    elif len(tmp_tup) > 0:
        space_add = space + tmp_tup[0]
        return tup_combinations(tmp_tup[1:], space_add) + tup_combinations(tmp_tup[1:], space)
    else:
        return 0


min_containers = 999
num_min_containers = 0


# Part 2
def tup_combo_min(available_tup, space, num_cont):
    tmp_tup = available_tup[:]
    global min_containers, num_min_containers
    if space == 150:
        if num_cont == min_containers:
            num_min_containers += 1
            return 1
        elif num_cont < min_containers:
            min_containers = num_cont
            num_min_containers = 1
            return 1
        else:
            return 0
    elif space > 150:
        return 0
    elif len(tmp_tup) > 0:
        space_add = space + tmp_tup[0]
        return tup_combo_min(tmp_tup[1:], space_add, num_cont + 1) + tup_combo_min(tmp_tup[1:], space, num_cont)
    else:
        return 0


print(tup_combo_min(tupperware, 0, 0))
print(min_containers)
print(num_min_containers)

