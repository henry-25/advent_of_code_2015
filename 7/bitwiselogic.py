import pprint
# Part 1/2

results = dict()
bitwise_inst = dict()


with open("input.txt") as file:
    for line in file:
        line = line.strip('\t\n').split('->')
        instr = line[0].strip().split(' ')
        bitwise_inst[line[1].strip()] = instr


def evaluate_operation(key):
    try:
        ans = int(key)
        return ans
    except ValueError:
        pass

    if key not in results:
        operation = bitwise_inst[key]
        if len(operation) == 1:
            res = evaluate_operation(operation[0])
        else:
            if operation[0] == "NOT":
                res = evaluate_operation(operation[1]) ^ 65535
            elif operation[1] == "OR":
                res = evaluate_operation(operation[0]) | evaluate_operation(operation[2])
            elif operation[1] == "AND":
                res = evaluate_operation(operation[0]) & evaluate_operation(operation[2])
            elif operation[1] == "LSHIFT":
                res = evaluate_operation(operation[0]) << evaluate_operation(operation[2])
            elif operation[1] == "RSHIFT":
                res = evaluate_operation(operation[0]) >> evaluate_operation(operation[2])
        results[key] = res
    return results[key]


val_a = evaluate_operation("a")
results.clear()
results["b"] = val_a
print(evaluate_operation("a"))


