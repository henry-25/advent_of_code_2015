# Part 1

str_alt = '1113222113'
str_const = ''
i = 1

while i < 51:
    while str_alt:
        curr_ch = str_alt[0]
        num_shift = 1
        curr = 0
        while len(str_alt) > curr + 1 and str_alt[curr] == str_alt[curr + 1]:
            num_shift += 1
            curr += 1
        str_alt = str_alt[num_shift:]
        str_const += str(num_shift) + str(curr_ch)
    str_alt = str_const
    str_const = ''
    i += 1
    print(i)

print(str_alt)
print(len(str_alt))
