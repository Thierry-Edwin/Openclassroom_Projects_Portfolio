"""

Lecture et ecriture des données

"""


import csv


class Tool:
    def __init__(self):
        pass

    def read_data(self, file):
        data = []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(tuple(row))
            return data

    def write_data(self, file, data, result):
        with open(file, "w", newline='') as f:
            header = ['Name', 'Cost', 'Profit', 'Score']
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
