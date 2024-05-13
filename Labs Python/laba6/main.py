#1

with open("input.txt", "r") as file:
    numbers = file.read().split()
    numbers = [int(num) for num in numbers]

product = 1
for num in numbers:
    product *= num

with open("output.txt", "w") as file:
    file.write(str(product))

#2
with open("input1.txt", "r") as file:
    numbers = file.readlines()
    numbers = [int(num.strip()) for num in numbers]

numbers.sort()

with open("output1.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

#3
with open("children.txt", "r") as file:
    lines = file.readlines()

children = []
for line in lines:
    data = line.split()
    surname = data[0]
    name = data[1]
    age = int(data[2])

children.append((surname, name, age))

children.sort(key=lambda x: x[2]) # Сортировка по возрасту

with open("children.txt", "r") as file:
    lines = file.readlines()

children = []
for line in lines:
    data = line.split()
    surname = data[0]
    name = data[1]
    age = int(data[2])

    children.append((surname, name, age))

children.sort(key=lambda x: x[2])

youngest = children[0]
oldest = children[-1]


with open("youngest.txt", "w") as file:
    file.write(f"{youngest[0]} {youngest[1]} {youngest[2]}")

with open("oldest.txt", "w") as file:
    file.write(f"{oldest[0]} {oldest[1]} {oldest[2]}")