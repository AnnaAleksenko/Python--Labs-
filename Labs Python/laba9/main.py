import numpy as np
#1

# Чтение матрицы из файла
matrix = np.loadtxt('matrix.txt', delimiter=',')


# Сумма всех элементов
sum_matrix = np.sum(matrix)

# Максимальный и минимальный элементы
max_matrix = np.max(matrix)
min_matrix = np.min(matrix)

print("Сумма всех элементов:", sum_matrix)
print("Максимальный элемент:", max_matrix)
print("Минимальный элемент:", min_matrix)

#2


def run_length_encoding(x):
    # Инициализация переменных
    values = []
    counts = []
    current_value = x[0]
    current_count = 1

    # Проход по вектору
    for i in range(1, len(x)):
        if x[i] == current_value:
            current_count += 1
        else:
            values.append(current_value)
            counts.append(current_count)
            current_value = x[i]
            current_count = 1

    # Добавление последней серии
    values.append(current_value)
    counts.append(current_count)

    return np.array(values), np.array(counts)


# Пример использования
x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = run_length_encoding(x)
print("Values:", values)
print("Counts:", counts)

#3

# Генерация массива случайных чисел нормального распределения
array = np.random.normal(size=(10, 4))

# Нахождение минимального, максимального, среднего значений и стандартного отклонения
min_value = np.min(array)
max_value = np.max(array)
mean_value = np.mean(array)
std_value = np.std(array)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = array[:5]

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_value)
print("Первые 5 строк:", first_five_rows)

#4
import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
zero_indices = np.where(x == 0)[0] # находим индексы нулевых элементов
nonzero_indices = zero_indices[zero_indices < len(x)-1] + 1 # находим индексы элементов, следующих за нулевыми
if len(nonzero_indices) > 0:
    nonzero_values = x[nonzero_indices] # находим значения элементов, следующих за нулевыми
    max_value = np.max(nonzero_values) # находим максимальное значение среди элементов, следующих за нулевыми
else:
    max_value = 0

print("Максимальный элемент перед нулевыми элементами:", max_value)

#5
from scipy.stats import multivariate_normal

def log_density(X, m, C):
    # Вычисление логарифма плотности многомерного нормального распределения
    D = X.shape[1]
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    X_m = X - m
    log_densities = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C) + np.sum(X_m @ inv_C * X_m, axis=1))

    return log_densities


# Генерация данных
m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 1]])
X = np.random.multivariate_normal(m, C, size=10000)

# Вычисление логарифма плотности многомерного нормального распределения
log_densities = log_density(X, m, C)
scipy_log_densities = multivariate_normal(m, C).logpdf(X)

# Сравнение результатов
print("Среднее значение ошибки:", np.mean(np.abs(log_densities - scipy_log_densities)))

#6

# Создание массива
a = np.arange(16).reshape(4,4)

# Поменять местами строки 1 и 3
a[[0, 2]] = a[[2, 0]]

print(a)

#7

# Загрузка данных
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Столбец species
species_column = iris[:, -1]

# Уникальные значения и их количество
unique_values, unique_counts = np.unique(species_column, return_counts=True)

print("Уникальные значения:", unique_values)
print("Количество уникальных значений:", unique_counts)


#8

# Вектор
x = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])

# Индексы ненулевых элементов
nonzero_indices = np.where(x != 0)[0]
print("Индексы ненулевых элементов:", nonzero_indices)