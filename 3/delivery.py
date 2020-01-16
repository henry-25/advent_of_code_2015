# Part 1

houses_visited = {(0, 0): 1}
curr_loc = [0, 0]
num_houses = 1

with open("input.txt") as file:
    for line in file:
        for ch in line:
            if ch == '^':
                curr_loc[0] -= 1
            elif ch == 'v':
                curr_loc[0] += 1
            elif ch == '<':
                curr_loc[1] -= 1
            elif ch == '>':
                curr_loc[1] += 1
            else:
                print('Invalid char: ', ch)
            cl = (curr_loc[0], curr_loc[1])
            if houses_visited.get(cl):
                houses_visited[cl] = houses_visited.get(cl) + 1
            else:
                houses_visited[cl] = 1
                num_houses += 1

# Part 2

houses_visited = {(0, 0): 1}
curr_loc_hum = [0, 0]
curr_loc_robot = [0, 0]
turn = "hum"
num_houses = 1

with open("input.txt") as file:
    for line in file:
        for ch in line:
            if turn == "hum":
                if ch == '^':
                    curr_loc_hum[0] -= 1
                elif ch == 'v':
                    curr_loc_hum[0] += 1
                elif ch == '<':
                    curr_loc_hum[1] -= 1
                elif ch == '>':
                    curr_loc_hum[1] += 1
                else:
                    print('Invalid char: ', ch)
                cl = (curr_loc_hum[0], curr_loc_hum[1])
                if houses_visited.get(cl):
                    houses_visited[cl] = houses_visited.get(cl) + 1
                else:
                    houses_visited[cl] = 1
                    num_houses += 1
                turn = "robo";
            else:
                if ch == '^':
                    curr_loc_robot[0] -= 1
                elif ch == 'v':
                    curr_loc_robot[0] += 1
                elif ch == '<':
                    curr_loc_robot[1] -= 1
                elif ch == '>':
                    curr_loc_robot[1] += 1
                else:
                    print('Invalid char: ', ch)
                cl = (curr_loc_robot[0], curr_loc_robot[1])
                if houses_visited.get(cl):
                    houses_visited[cl] = houses_visited.get(cl) + 1
                else:
                    houses_visited[cl] = 1
                    num_houses += 1
                turn = "hum"

print(num_houses)
