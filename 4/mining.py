import hashlib

# Part 1

initial_append = 1

while True:
    str_temp = "bgvyzdsv" + str(initial_append)
    result = hashlib.md5(str_temp.encode())
    if result.hexdigest()[:5] == "00000":
        print("Found the 5-digit answer: ", initial_append)
        break
    initial_append += 1

# Part 2

initial_append = 1

while True:
    str_temp = "bgvyzdsv" + str(initial_append)
    result = hashlib.md5(str_temp.encode())
    if result.hexdigest()[:6] == "000000":
        print("Found the 6-digit answer: ", initial_append)
        break
    initial_append += 1

