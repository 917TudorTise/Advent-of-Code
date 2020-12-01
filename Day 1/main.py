f = open("scratch.txt", "r")
g = open("solution.txt", "a")

numbers = []

for x in f:
    numbers.append(int(x))

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            g.write(str(numbers[i] * numbers[j]))

f.close()
g.close()
