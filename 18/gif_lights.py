import pprint
import copy

lights_grid = []

with open('input.txt') as file:
    for line_num, line in enumerate(file):
        line = line.strip()
        lights_grid.append([])
        for col_num, ch in enumerate(line):
            lights_grid[line_num].append(ch)


def check_adjacent(line_number, column_number, lights):
    lights_on = 0
    if line_number > 0:
        if column_number > 0:
            # Top Left
            if lights[line_number - 1][column_number - 1] == '#':
                lights_on += 1
        if column_number < len(lights_grid) - 1:
            # Top Right
            if lights[line_number - 1][column_number + 1] == '#':
                lights_on += 1
        # Middle Top
        if lights[line_number - 1][column_number] == '#':
            lights_on += 1
    if line_number < len(lights_grid) - 1:
        if column_number < len(lights_grid) - 1:
            # Bottom Right
            if lights[line_number + 1][column_number + 1] == '#':
                lights_on += 1
        if column_number > 0:
            # Bottom Left
            if lights[line_number + 1][column_number - 1] == '#':
                lights_on += 1
        # Middle Bottom
        if lights[line_number + 1][column_number] == '#':
            lights_on += 1
    if column_number > 0:
        # Middle Left
        if lights[line_number][column_number - 1] == '#':
            lights_on += 1
    if column_number < len(lights_grid) - 1:
        # Middle Right
        if lights[line_number][column_number + 1] == '#':
            lights_on += 1
    return lights_on


def take_step(initial_state):
    tmp_state = copy.deepcopy(initial_state)
    for l_num, l in enumerate(tmp_state):
        for c_num, c in enumerate(l):
            adjacent_lights = check_adjacent(l_num, c_num, initial_state)
            corner_spots = [(0, 0), (0, len(l) - 1), (len(l) - 1, 0), (len(l) - 1, len(l) - 1)]
            if (l_num, c_num) in corner_spots:
                tmp_state[l_num][c_num] = '#'
            elif c == '#':
                if adjacent_lights == 2 or adjacent_lights == 3:
                    tmp_state[l_num][c_num] = '#'
                else:
                    tmp_state[l_num][c_num] = '.'
            else:
                if adjacent_lights == 3:
                    tmp_state[l_num][c_num] = '#'
                else:
                    tmp_state[l_num][c_num] = '.'
    return tmp_state


# Part 1
# Part 2 input changed to make corner spots all lights on
step_num = 0
while step_num < 100:
    lights_grid = take_step(lights_grid)
    step_num += 1

lights_on = 0
for i in lights_grid:
    for j in i:
        if j == '#':
            lights_on += 1

pprint.pprint(lights_grid)
print(lights_on)
