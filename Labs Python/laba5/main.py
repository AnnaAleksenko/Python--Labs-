# 1
# Принимаем список чисел в виде строки, разделенной запятыми
numbers = input("Введите список список чисел в виде строки, разделенной запятыми: ")

# Преобразуем строку в список, удаляя пробелы и приводя элементы к целочисленному типу
numbers = [int(n.strip()) for n in numbers.split(",")]

# Преобразуем список в множество, чтобы убрать повторяющиеся элементы
numbers = set(numbers)

# Выводим количество элементов в множестве, что соответствует количеству различных чисел в списке
print("Количество элементов в множестве, что соответствует количеству различных чисел в списке:", len(numbers))

# 2
# Принимаем два множества чисел в виде строк, разделенных запятыми и заключенных в фигурные скобки
set1 = input("Введите первое множество чисел в виде строк, разделенных запятыми и заключенных в фигурные скобки: ")
set2 = input("Введите второе множество чисел в виде строк, разделенных запятыми и заключенных в фигурные скобки: ")

# Преобразуем строки в множества, удаляя пробелы и приводя элементы к целочисленному типу
set1 = {int(n.strip()) for n in set1[1:-1].split(",")}
set2 = {int(n.strip()) for n in set2[1:-1].split(",")}

# Проверяем, является ли первое множество подмножеством второго, используя метод issubset
# Выводим True или False в зависимости от результата
print("Является ли первое множество подмножеством второго:", set1.issubset(set2) and set1 != set2)

# 3
# Принимаем количество названных городов в виде натурального числа
n = int(input("Введите количество названных городов: "))

# Создаем пустое множество для хранения названных городов
cities = set()

# В цикле n раз принимаем название города и добавляем его в множество, если он еще не был назван
# Если город уже был назван, выводим REPEAT и прерываем цикл
for i in range(n):
    city = input("Введите название города: ")
    if city in cities:
        print("REPEAT")
        break
    else:
        cities.add(city)

# Принимаем новый город и проверяем, есть ли он в множестве названных городов
# Если есть, выводим REPEAT, если нет, выводим OK
new_city = input("Введите новый город: ")
if new_city in cities:
    print("REPEAT")
else:
    print("OK")
