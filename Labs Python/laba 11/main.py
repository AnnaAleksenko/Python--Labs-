#1
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square


# генерируем прямоугольный сигнал
t = np.linspace(0, 1, 1000)
x = square(2 * np.pi * 5 * t)

# отображаем сигнал
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Square Wave')
plt.show()

#2
# генерация данных для нормального распределения
mu, sigma = 0, 0.1  # среднее значение и стандартное отклонение
data = np.random.normal(mu, sigma, 1000)

# построение гистограммы распределения
plt.hist(data, bins=20)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Normal Distribution')
plt.show()

#3


with open('passengers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок
    data = [int(row[1]) for row in reader]

# проверка длины списка данных
if len(data) == 0:
    print("Data is empty. Please check the file.")
    exit()

# построение графика потока за все время
plt.plot(data)
plt.xlabel('Month')
plt.ylabel('Passengers')
plt.title('Airline Passengers')
plt.show()

# построение гистограммы по месяцам в 1951 - 1955 гг.
years = ['1951', '1952', '1953', '1954', '1955']
data_by_year = []
for year in years:
    start_index = 12 * (int(year) - 1951)
    end_index = start_index + 12
    if end_index > len(data):
        print("Data is incomplete for year . Please check the file.".format(year))
        exit()
    data_by_year.append(data[start_index:end_index])

fig, axs = plt.subplots(5, 1, figsize=(8, 12))
for i in range(5):
    axs[i].hist(data_by_year[i], bins=20)
    axs[i].set_xlabel('Passengers')
    axs[i].set_ylabel('Frequency')
    axs[i].set_title(years[i])
plt.tight_layout()
plt.show()
