import os.path
import json


class Model():
    def __init__(self, filename=os.path.join(os.path.dirname(__file__), 'config.json')):
        self.filename = filename
        self.__read_file()

    def __read_file(self):
        filename = self.filename

        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file)

        with open(filename, 'r') as file:
            try:
                data = json.load(file)
            except:
                backup_filename = filename + '.bkp'
                with open(backup_filename, 'w') as backup_file:
                    backup_file.write(file.read())
                data = []

        self.data = data

    def __write_file(self):
        filename = self.filename
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def get_data(self):
        self.__read_file()
        return self.data

    def save_data(self, **entries):
        self.__read_file()
        self.data.append(entries)
        self.__write_file()

    def delete_data(self, index):
        del self.data[index]
        self.__write_file()
