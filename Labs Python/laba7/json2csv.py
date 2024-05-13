import json
import csv
import sys
import os

def json_to_csv(json_file):
    # Открытие JSON файла
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Получение имени JSON файла без расширения
    file_name = os.path.splitext(json_file)[0]

    # Создание CSV файла с тем же именем
    csv_file = f"{file_name}.csv"

    # Открытие CSV файла для записи
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Запись заголовков CSV файла из ключей первого объекта в JSON файле
        writer.writerow(data[0].keys())

        # Запись данных в CSV файл
        for item in data:
            writer.writerow(item.values())

    print(f"JSON файл успешно преобразован в CSV. Результат сохранен в файле: {csv_file}")

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки (имя JSON файла)
    if len(sys.argv) < 2:
        print("Необходимо указать имя JSON файла в качестве аргумента командной строки.")
    else:
        json_file = sys.argv[1]
        json_to_csv(json_file)