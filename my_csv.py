import csv
import os

class CSV():

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, array):
        with open(os.path.join(self.file_path), 'w') as f:
            write = csv.writer(f)
            write.writerows(array)

    def read(self):
        array = []
        with open(os.path.join(self.file_path), 'r') as f:
            read = csv.reader(f)
            array = list(read)
        return array