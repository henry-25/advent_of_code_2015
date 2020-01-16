# Part 1


def increment_string(org_string):
    curr_ch = len(org_string) - 1
    if len(org_string) > 0:
        while True:
            if org_string[curr_ch] == 'z' and curr_ch > -1:
                org_string = org_string[:curr_ch] + 'a' + org_string[curr_ch + 1:]
                curr_ch -= 1
            elif curr_ch > -1:
                org_string = org_string[:curr_ch] + chr(ord(org_string[curr_ch]) + 1) + org_string[curr_ch + 1:]
                return org_string
            else:
                return org_string


def check_pass_rules(org_string):
    inc, cant_overlap = False, False
    last_ch, two_back_ch = '', ''
    num_doubles, curr_ch = 0, 0
    while curr_ch < len(org_string):
        if curr_ch > 1:
            if org_string[curr_ch] == last_ch and cant_overlap is False:
                num_doubles += 1
                cant_overlap = True
                two_back_ch = last_ch
                last_ch = org_string[curr_ch]
                curr_ch += 1
            elif ord(two_back_ch) + 2 == ord(last_ch) + 1 == ord(org_string[curr_ch]):
                inc = True
                cant_overlap = False
                two_back_ch = last_ch
                last_ch = org_string[curr_ch]
                curr_ch += 1
            else:
                cant_overlap = False
                two_back_ch = last_ch
                last_ch = org_string[curr_ch]
                curr_ch += 1
        elif curr_ch == 1:
            if org_string[curr_ch] == last_ch:
                num_doubles += 1
                cant_overlap = True
                two_back_ch = last_ch
                last_ch = org_string[curr_ch]
                curr_ch += 1
            else:
                two_back_ch = last_ch
                last_ch = org_string[curr_ch]
                curr_ch += 1
        else:
            last_ch = org_string[curr_ch]
            curr_ch += 1
    return inc, num_doubles


def check_and_change_forb_letters(org_string):
    change_to_a = False
    curr_ch = 0
    while curr_ch < len(org_string):
        if change_to_a:
            org_string = org_string[:curr_ch] + 'a' + org_string[curr_ch + 1:]
            curr_ch += 1
        elif org_string[curr_ch] in ['i', 'o', 'l']:
            org_string = org_string[:curr_ch] + chr(ord(org_string[curr_ch]) + 1) + org_string[curr_ch + 1:]
            change_to_a = True
            curr_ch += 1
        else:
            curr_ch += 1
    return org_string


str_p1 = "hxbxwxba"
str_p2 = "hxbxxyzz"

while True:
    str_p2 = increment_string(str_p2)
    str_p2 = check_and_change_forb_letters(str_p2)
    if check_pass_rules(str_p2) == (True, 2):
        print("Passed", str_p2)
        break