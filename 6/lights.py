# Part 1

# yard = [[False for j in range(1000)] for i in range(1000)]
#
# with open("input.txt") as file:
#     for line in file:
#         line = line.strip('\t\n')
#         line = line.split(' ')
#         if line[0] == "toggle":
#             start_point = line[1].split(',')
#             end_point = line[3].split(',')
#             start_point = [int(start_point[0]), int(start_point[1])]
#             end_point = [int(end_point[0]) + 1, int(end_point[1]) + 1]
#             for x in range(start_point[0], end_point[0]):
#                 for y in range(start_point[1], end_point[1]):
#                     yard[x][y] = not yard[x][y]
#         elif line[1] == "off":
#             start_point = line[2].split(',')
#             end_point = line[4].split(',')
#             start_point = [int(start_point[0]), int(start_point[1])]
#             end_point = [int(end_point[0]) + 1, int(end_point[1]) + 1]
#             for x in range(start_point[0], end_point[0]):
#                 for y in range(start_point[1], end_point[1]):
#                     yard[x][y] = False
#         else:
#             start_point = line[2].split(',')
#             end_point = line[4].split(',')
#             start_point = [int(start_point[0]), int(start_point[1])]
#             end_point = [int(end_point[0]) + 1, int(end_point[1]) + 1]
#             for x in range(start_point[0], end_point[0]):
#                 for y in range(start_point[1], end_point[1]):
#                     yard[x][y] = True
#
# lights_on = 0
#
# for l in range(1000):
#     for m in range(1000):
#         if yard[l][m]:
#             lights_on += 1
#
# print(lights_on)

# Part 2

yard = [[0 for j in range(1000)] for i in range(1000)]

with open("input.txt") as file:
    for line in file:
        line = line.strip('\t\n')
        line = line.split(' ')
        if line[0] == "toggle":
            start_point = line[1].split(',')
            end_point = line[3].split(',')
            start_point = [int(start_point[0]), int(start_point[1])]
            end_point = [int(end_point[0]) + 1, int(end_point[1]) + 1]
            for x in range(start_point[0], end_point[0]):
                for y in range(start_point[1], end_point[1]):
                    yard[x][y] += 2
        elif line[1] == "off":
            start_point = line[2].split(',')
            end_point = line[4].split(',')
            start_point = [int(start_point[0]), int(start_point[1])]
            end_point = [int(end_point[0]) + 1, int(end_point[1]) + 1]
            for x in range(start_point[0], end_point[0]):
                for y in range(start_point[1], end_point[1]):
                    if yard[x][y] != 0:
                        yard[x][y] -= 1
        else:
            start_point = line[2].split(',')
            end_point = line[4].split(',')
            start_point = [int(start_point[0]), int(start_point[1])]
            end_point = [int(end_point[0]) + 1, int(end_point[1]) + 1]
            for x in range(start_point[0], end_point[0]):
                for y in range(start_point[1], end_point[1]):
                    yard[x][y] += 1

lights_brightness = 0

for l in range(1000):
    for m in range(1000):
        lights_brightness += yard[l][m]

print(lights_brightness)