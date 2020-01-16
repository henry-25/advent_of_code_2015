# Part 1

floor = 0

with open("input.txt") as file:
    for line in file:
        for ch in line:
            if ch == '(':
                floor = floor + 1
            elif ch == ')':
                floor = floor - 1
            else:
                break

print("Final floor:", floor)

# Part 2

floor = 0
position = 0

with open("input.txt") as file:
    for line in file:
        for ch in line:
            if floor != -1:
                if ch == '(':
                    floor = floor + 1
                elif ch == ')':
                    floor = floor - 1
                else:
                    break
                position = position + 1

print("First basement:", position)
