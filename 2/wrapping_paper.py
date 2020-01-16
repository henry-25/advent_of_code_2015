# Part 1


def find_smallest_side(sides):
    smallest_area = sides[0] * sides[1]
    smallest_perimeter = 2 * sides[0] + 2 * sides[1]
    if sides[1] * sides[2] < smallest_area:
        smallest_area = sides[1] * sides[2]
    if sides[0] * sides[2] < smallest_area:
        smallest_area = sides[0] * sides[2]
    if 2 * sides[1] + 2 * sides[2] < smallest_perimeter:
        smallest_perimeter = 2 * sides[1] + 2 * sides[2]
    if 2 * sides[0] + 2 * sides[2] < smallest_perimeter:
        smallest_perimeter = 2 * sides[0] + 2 * sides[2]
    return smallest_area, smallest_perimeter


total_wrapping_paper = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip(' \n\t')
        dimensions = line.split('x')
        for ind, d in enumerate(dimensions):
            dimensions[ind] = int(d)
        total_paper = (2 * dimensions[0] * dimensions[1]) + (2 * dimensions[1] * dimensions[2]) + (2 * dimensions[0] * dimensions[2]) + find_smallest_side(dimensions)[0]
        total_wrapping_paper += total_paper

print(total_wrapping_paper)

# Part 2

total_ribbon_required = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip(' \n\t')
        dimensions = line.split('x')
        for ind, d in enumerate(dimensions):
            dimensions[ind] = int(d)
        ribbon_req = (dimensions[0] * dimensions[1] * dimensions[2]) + find_smallest_side(dimensions)[1]
        total_ribbon_required += ribbon_req

print(total_ribbon_required)
