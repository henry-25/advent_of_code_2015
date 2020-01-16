import pprint
# Part 1 answer 618
# Part 2 answer 601

seating_partners = {'Henry': []}
first_seated = ''
highest_happiness = 0

with open('input.txt') as file:
    for line in file:
        line = line.strip()[:-1].split(' ')
        source = line[0]
        seating_partners[source] = []
    file.seek(0)
    for line in file:
        line = line.strip()[:-1].split(' ')
        source = line[0]
        direction = line[2]
        units = int(line[3])
        recipient = line[10]
        if direction == 'gain':
            seating_partners[source].append((recipient, units))
        else:
            seating_partners[source].append((recipient, -units))
        if not ('Henry', 0) in seating_partners[source]:
            seating_partners[source].append(('Henry', 0))
        if not (source, 0) in seating_partners['Henry']:
            seating_partners['Henry'].append((source, 0))


def dinner_table_knights(currently_seating, potential_partners, seated_individuals, happiness):
    tmp_seated = seated_individuals[:]
    tmp_seated.append(currently_seating)
    global highest_happiness, first_seated
    if len(tmp_seated) == len(potential_partners.keys()):
        # Add initial and last seated happiness
        happiness += [happy[1] for happy in potential_partners[first_seated] if happy[0] == currently_seating][0]
        happiness += [happy[1] for happy in potential_partners[currently_seating] if happy[0] == first_seated][0]
        if happiness > highest_happiness:
            highest_happiness = happiness
        return
    for ppl in potential_partners[currently_seating]:
        if ppl[0] not in seated_individuals:
            result = [happy[1] for happy in potential_partners[ppl[0]] if happy[0] == currently_seating][0]
            happiness_gain = ppl[1] + result
            dinner_table_knights(ppl[0], potential_partners, tmp_seated, happiness + happiness_gain)


pprint.pprint(seating_partners)
first_seated = 'Henry'
dinner_table_knights('Henry', seating_partners, [], 0)
print(highest_happiness)
