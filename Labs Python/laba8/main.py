import csv
import os
import random


class CSVFile:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.data.append(row)

    def show(self, display_type='top', num_rows=5, separator=','):
        if display_type == 'top':
            for row in self.data[:num_rows]:
                print(separator.join(row))
        elif display_type == 'bottom':
            for row in self.data[-num_rows:]:
                print(separator.join(row))
        elif display_type == 'random':
            random_rows = random.sample(self.data, num_rows)
            for row in random_rows:
                print(separator.join(row))
        else:
            print("Invalid display type")

    def info(self):
        num_rows = len(self.data) - 1
        num_columns = len(self.data[0])
        print(f"Number of rows and columns: {num_rows}x{num_columns}")

        headers = self.data[0]
        for col_idx in range(num_columns):
            col_values = [row[col_idx] for row in self.data[1:]]
            non_empty_values = [val for val in col_values if val.strip()]
            qty_non_empty = len(non_empty_values)
            col_type = type(non_empty_values[0]).__name__
            print(f"{headers[col_idx]} {qty_non_empty} {col_type}")

    def del_nan(self):
        self.data = [row for row in self.data if all(val.strip() for val in row)]

    def make_ds(self):
        learning_data = random.sample(self.data[1:], int(0.7 * len(self.data)))
        testing_data = [row for row in self.data[1:] if row not in learning_data]

        os.makedirs('workdata/Learning', exist_ok=True)
        os.makedirs('workdata/Testing', exist_ok=True)

        with open('workdata/Learning/train.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(self.data[0])
            csv_writer.writerows(learning_data)

        with open('workdata/Testing/test.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(self.data[0])
            csv_writer.writerows(testing_data)


file = CSVFile('data.csv')
file.show(display_type='top', num_rows=5, separator=',')
file.info()
file.del_nan()
file.make_ds()