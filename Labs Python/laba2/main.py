# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

 #1
def Triangle(n):
    pattern = ["*"]
    for i in range(n):
        sp = " " * (2**i)
        pattern = [sp + x + sp for x in pattern] + [x + " " + x for x in pattern]
    print("\n".join(pattern))


Triangle(int(input("Программа, в которой с помощью псевдографики состоящей из звездочек * выводится треугольник Серпинского\n"
                   "Введите натуральное число:")))

#2
n = int(input("Программа, которая выводит n строк треугольника Паскаля.\n "
                 "Введите натуральное число:"))

for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        print(' ', end='')

    # first element is 1
    C = 1
    for j in range(1, i + 1):
        # first value in a line is 1
        print(' ', C, sep='', end='')

        C = C * (i - j) // j
    print()
