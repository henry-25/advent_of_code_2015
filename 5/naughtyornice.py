# Part 1

nice = 0

vowels_array = ['a', 'e', 'i', 'o', 'u']
forbidden_strings = ["ab", "cd", "pq", "xy"]

with open("input.txt") as file:
    for line in file:
        num_vowels = 0
        several_vowels, double_character, is_naughty = False, False, False
        last_char = ''
        for ch in line:
            if ch in vowels_array:
                num_vowels += 1
                if num_vowels > 2:
                    several_vowels = True
            if last_char == ch:
                double_character = True
            if last_char + ch in forbidden_strings:
                is_naughty = True
                break
            last_char = ch
        if not is_naughty and several_vowels and double_character:
            nice += 1

# Part 2

nice = 0


def check_reoccurence(str_org, str_remaining):
    if str_org == str_remaining[:2]:
        return True
    if len(str_remaining) > 2:
        if check_reoccurence(str_org, str_remaining[1:]):
            return True
    return False


with open("input.txt") as file:
    for line in file:
        last_char = ''
        char_before_last = ''
        double_char_occur, repeat_one_between = False, False
        for num, ch in enumerate(line):
            if check_reoccurence(last_char + ch, line[num + 1:]):
                double_char_occur = True
            if char_before_last == ch:
                repeat_one_between = True
            char_before_last = last_char
            last_char = ch
        if double_char_occur and repeat_one_between:
            nice += 1
