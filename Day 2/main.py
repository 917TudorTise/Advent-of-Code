
f = open("data1.txt", "r")

nr_valid_pass = 0

while True:

    is_ok = True

    line = f.readline()
    if not line:
        break
    aux = line.split("-")

    limits = [int(aux[0]), int(aux[1].split(" ")[0])]
    char = line.split(" ")[1].split(":")[0]
    password = line.split(" ")[2]

    number_of_occurrences = 0
    for each in password:
        if each == char:
            number_of_occurrences +=1

    if number_of_occurrences < limits[0] or number_of_occurrences > limits[1]:
        is_ok = False

    if is_ok:
        nr_valid_pass +=1



print("There are ", nr_valid_pass, " number of valid passwords")
