import csv
import os


def read_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as csv_file:
        return [
            item
            for item in csv.reader(csv_file)
        ]


def get_column_data(filename, column_num):
    '''Get needed values from specific column'''
    with open(filename, "r", newline="", encoding="utf-8") as csv_file:
        return [
            x[column_num]
            for x in csv.reader(csv_file)
        ]


def create_new_csv(new_filename, names_arr):
    '''Take values from second column and create new csv from that values'''
    with open(new_filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, escapechar=" ", quoting=csv.QUOTE_NONE)
        for name in names_arr:
            writer.writerow([name])

    return print(f'File {new_filename} was successfully created.')
