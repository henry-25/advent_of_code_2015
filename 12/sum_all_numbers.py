import json
# Part 1


def unpack_dict(data_dict):
    total_val_dict = 0
    for el in data_dict.keys():
        if isinstance(data_dict[el], list):
            total_val_dict += unpack_list(data_dict[el])
        elif isinstance(data_dict[el], dict):
            total_val_dict += unpack_dict(data_dict[el])
        elif isinstance(data_dict[el], int):
            total_val_dict += data_dict[el]
        elif isinstance(data_dict[el], str):
            if data_dict[el] == 'red':
                return 0
    return total_val_dict


def unpack_list(data_list):
    total_val_list = 0
    for el in data_list:
        if isinstance(el, list):
            total_val_list += unpack_list(el)
        elif isinstance(el, dict):
            total_val_list += unpack_dict(el)
        elif isinstance(el, int):
            total_val_list += el
    return total_val_list


with open('input.txt') as file:
    data = json.load(file)
    total_val = 0
    if isinstance(data, dict):
        total_val += unpack_dict(data)
    elif isinstance(data, list):
        total_val += unpack_list(data)
    print(total_val)