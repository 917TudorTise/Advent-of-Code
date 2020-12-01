f = open("scratch.txt", "r")
sol1 = open("solution.txt", "a")
sol2 = open("solution2.txt", "a")

numbers = []

for x in f:
    numbers.append(int(x))

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            sol1.write(str(numbers[i] * numbers[j]))

for i in range(len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                sol2.write(str(numbers[i] * numbers[j] * numbers[k]))

f.close()
sol1.close()
sol2.close()
