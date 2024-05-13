# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1

print("Программа сравнивает между собой и возвращает количество совпадающих \n"
      "Введите 3 числа.")
x, y, z=str(input()).split()
if (x == y) and (y == z) and (x == z):
    print(3, "-Совпадают все числа")
elif (x == y) or (y == z) or (x == z):
    print(2,"-Cовпадают 2 числа")
else:
    print(0, "-Все числа различны")

#2.1.1

print("Вывод лестницы из n ступенек\n"
      "Введите число.")
x = int(input("Введите натуральное число:"))
if x > 0:
    for i in range(1, x+1):
        for j in range(1, i + 1):
            print(j, sep="", end="")
        print()

#2.1.2

print("Вывод лестницы из n ступенек\n"
      "Введите число.")
n = int(input())
x = ""
for i in range(1, n + 1):
    x = x + str(i)
    print(x)
    

#2.2

print("Вывод пирамиды из n ступенек\n"
      "Введите число.")
n = int(input()) + 1
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print(*range(1, i),*range(1,i-1)[::-1], sep='')


