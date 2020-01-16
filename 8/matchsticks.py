# Part 1

# num_code_ch = 0
# num_mem_ch = 0
#
#
# with open("input.txt") as file:
#     for line in file:
#         line = line.strip(' \t\n')
#         inline = 1
#         num_code_ch += 2
#         while inline < len(line):
#             if inline != len(line) - 1:
#                 if line[inline] == '\\' and line[inline + 1] in ('\\', '"'):
#                     num_code_ch += 2
#                     num_mem_ch += 1
#                     inline += 2
#                 elif line[inline] == '\\' and line[inline + 1] == 'x':
#                     num_code_ch += 4
#                     num_mem_ch += 1
#                     inline += 4
#                 else:
#                     num_code_ch += 1
#                     num_mem_ch += 1
#                     inline += 1
#             else:
#                 inline += 1
#
# print(num_code_ch - num_mem_ch)

# Part 2

num_ch_original = 0
num_ch_new = 0


def find_new_chars(line_rec):
    print(line_rec)
    if len(line_rec) == 1 and line_rec[0] == '"':
        return 3
    elif len(line_rec) == 1:
        return 1
    elif line_rec[0] not in ('"', '\\'):
        return 1 + find_new_chars(line_rec[1:])
    elif line_rec[0] == '"':
        return 3 + find_new_chars(line_rec[1:])
    elif line_rec[0] == '\\' and line_rec[1] == '"':
        return 4 + find_new_chars(line_rec[2:])


with open("input_example.txt") as file:
    for line in file:
        line = line.strip(' \t\n')
        num_ch_new += find_new_chars(line)
        print(num_ch_new)
        for ch in line:
            num_ch_original += 1