#0
def find_greater(lsd0):
    return [lsd0[i] for i in range(1, len(lsd0)) if lsd0[i] > lsd0[i-1]]

lsd0 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print("Список с числами:",lsd0)
print("Вывод элементов списка, которые больше предыдущего, в виде отдельного списка:",find_greater(lsd0))
#1
def swap_min_max(lsh11):
    min_idx = lsh11.index(min(lsh11))
    max_idx = lsh11.index(max(lsh11))
    lsh11[min_idx], lsh11[max_idx] = lsh11[max_idx], lsh11[min_idx]
    return lsh11

lsh11 = [1, 2, 3, 4, 5]
print("Список с числами:",lsh11)
print("Поменяли местами наибольший и наименьший элемент:",swap_min_max(lsh11))
#2
def count_common(lst1, lst2):
    return len(set(lst1) & set(lst2))

lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print("Список 1",lst1)
print("Список 2",lst2)
print("Определили количество общих чисел из первого и второго списка:",count_common(lst1, lst2))
#3
def count_duplicates(lst3):
    d = {}
    for item in lst3:
        if item not in d:
            d[item] = 0
        d[item] += 1
    return [d[item] for item in d]

lst3 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
print("Cписок строк:",lst3)
print("Вывод количества повторений данных строк в списке:",count_duplicates(lst3))
