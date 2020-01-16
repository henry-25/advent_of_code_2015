import pprint, sys

# Part 1
# 719 too high

# Part 2
# 803 too low

curr_shortest = 100000
curr_longest = 0
routes = {}

with open('input.txt') as file:
    for line in file:
        line = line.split(' ')
        routes[line[0]] = []
        routes[line[2]] = []
    file.seek(0)
    for line in file:
        line = line.split(' ')
        routes[line[0]].append((line[2], line[4].strip()))
        routes[line[2]].append((line[0], line[4].strip()))


def shortest_path(node, poss_paths, length, visited_places):
    tmp_visit = visited_places[:]
    tmp_visit.append(node)
    global curr_shortest
    if len(tmp_visit) == 8:
        if length < curr_shortest:
            print(tmp_visit, length)
            curr_shortest = length
        return
    for i in poss_paths[node]:
        if i[0] not in tmp_visit and length + int(i[1]) < curr_shortest:
            shortest_path(i[0], poss_paths, length + int(i[1]), tmp_visit)


def longest_path(node, poss_paths, length, visited_places):
    tmp_visit = visited_places[:]
    tmp_visit.append(node)
    global curr_longest
    if len(tmp_visit) == 8:
        if length > curr_longest:
            print(tmp_visit, length)
            curr_longest = length
        return
    for i in poss_paths[node]:
        print(curr_longest, i, tmp_visit)
        if i[0] not in tmp_visit:
            longest_path(i[0], poss_paths, length + int(i[1]), tmp_visit)



vdest_short = []
vdest_long = []
for key in routes.keys():
    # shortest_path(key, routes, 0, vdest_short)
    longest_path(key, routes, 0, vdest_long)


print(curr_shortest)
print(curr_longest)
