import pprint, math

reindeer_info = {}
dist_traveled = {}
points = {}

with open('input.txt') as file:
    for line in file:
        info = line.strip().split(' ')
        curr_reindeer = info[0]
        dist_traveled[curr_reindeer] = 0
        points[curr_reindeer] = {}
        points[curr_reindeer]['is_moving'] = True
        points[curr_reindeer]['turns_left'] = int(info[6])
        points[curr_reindeer]['curr_position'] = 0
        points[curr_reindeer]['score'] = 0
        reindeer_info[curr_reindeer] = {}
        reindeer_info[curr_reindeer]['speed'] = int(info[3])
        reindeer_info[curr_reindeer]['duration'] = int(info[6])
        reindeer_info[curr_reindeer]['rest'] = int(info[13])

# Part 1

# for reindeer in reindeer_info:
#     duration, rest, speed = reindeer_info[reindeer]['duration'], reindeer_info[reindeer]['rest'], reindeer_info[reindeer]['speed']
#     time_seg = duration + rest
#     num_cycles = math.floor(2503 / time_seg)
#     time_eclipsed = num_cycles * time_seg
#     time_remaining = 2503 - time_eclipsed
#     dist_traveled[reindeer] = num_cycles * duration * speed
#     if duration < time_remaining:
#         dist_traveled[reindeer] += duration * speed
#     else:
#         dist_traveled[reindeer] += time_remaining * speed

# Part 2 647 is too low

i = 0
while i < 2504:
    furthest_reindeer = 0
    leading_reindeer = []
    for reindeer in reindeer_info:
        if points[reindeer]['is_moving']:
            points[reindeer]['curr_position'] += reindeer_info[reindeer]['speed']
            points[reindeer]['turns_left'] -= 1
            if points[reindeer]['turns_left'] == 0:
                points[reindeer]['is_moving'] = False
                points[reindeer]['turns_left'] = reindeer_info[reindeer]['rest']
        else:
            points[reindeer]['turns_left'] -= 1
            if points[reindeer]['turns_left'] == 0:
                points[reindeer]['is_moving'] = True
                points[reindeer]['turns_left'] = reindeer_info[reindeer]['duration']
        if points[reindeer]['curr_position'] > furthest_reindeer:
            furthest_reindeer = points[reindeer]['curr_position']
            leading_reindeer = [reindeer]
        elif points[reindeer]['curr_position'] == furthest_reindeer:
            leading_reindeer.append(reindeer)
    for lr in leading_reindeer:
        points[lr]['score'] += 1
    # if i < 5 or i > 2500:
    #     for reindeer in reindeer_info:
    #         print(i, reindeer, 'score:', points[reindeer]['score'], 'position:', points[reindeer]['curr_position'])
        # print(i, 'Comet', points['Comet']['score'], 'Rudolph', points['Rudolph']['score'])
    i += 1

pprint.pprint(points)





