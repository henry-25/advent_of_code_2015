import pprint

# Part 1


class Sue:
    def __init__(self, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes


desired_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with open('input.txt') as file:
    for line in file:
        line = line.replace(',', '').replace(':', '').strip().split(' ')
        # Part 1
        # if desired_sue[line[2]] == int(line[3]) and desired_sue[line[4]] == int(line[5]) and desired_sue[line[6]] == int(line[7]):
        #     print(line)
        # Part 2
        attr = [(line[2], int(line[3])), (line[4], int(line[5])), (line[6], int(line[7]))]
        correct_sue = True
        for a in attr:
            if correct_sue:
                if a[0] == 'cats':
                    if a[1] < desired_sue['cats']:
                        correct_sue = False
                elif a[0] == 'trees':
                    if a[1] < desired_sue['trees']:
                        correct_sue = False
                elif a[0] == 'pomeranians':
                    if a[1] > desired_sue['pomeranians']:
                        correct_sue = False
                elif a[0] == 'goldfish':
                    if a[1] > desired_sue['goldfish']:
                        correct_sue = False
                else:
                    if a[1] != desired_sue[a[0]]:
                        correct_sue = False
        if correct_sue:
            print('True', line)


pprint.pprint(desired_sue)
