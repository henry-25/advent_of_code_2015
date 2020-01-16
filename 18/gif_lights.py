import pprint

# Part 1


def get_neighbors(curr_x, curr_y, lg):
    num_neighbors = 0
    # Top left
    if curr_x > 0 and curr_y > 0 and lg[curr_y - 1][curr_x - 1] == '#':
        num_neighbors += 1
    # Top middle
    if curr_y > 0 and lg[curr_y - 1][curr_x] == '#':
        num_neighbors += 1
    # Top right
    if curr_x < len(lg) and curr_y > 0 and lg[curr_y - 1][curr_x + 1] == '#':
        num_neighbors += 1
    # Middle right
    if curr_x < len(lg) and lg[curr_y][curr_x + 1] == '#':
        num_neighbors += 1
    # Bottom right
    if curr_x < len(lg) and curr_y < len(lg) and lg[curr_y + 1][curr_x + 1] == '#':
        num_neighbors += 1
    # Bottom middle
    if curr_y < len(lg) and lg[curr_y + 1][curr_x] == '#':
        num_neighbors += 1
    # Bottom left
    if curr_x > 0 and curr_y < len(lg) and lg[curr_y + 1][curr_x - 1] == '#':
        num_neighbors += 1
    # Middle left
    if curr_x > 0 and lg[curr_y][curr_x - 1] == '#':
        num_neighbors += 1
    return num_neighbors


lights_grid = [['.' for i in range(0, 100)] for j in range(0, 100)]

with open('input.txt') as file:
    for n, line in enumerate(file):
        line = line.strip()
        for t, ch in enumerate(line):
            lights_grid[n][t] = ch

tmp_grid = lights_grid[:]

print(len(tmp_grid))
