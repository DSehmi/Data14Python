import csv


class Iris:
    def __init__(self, filename):
        raw_data = self.load_data(filename)
        self.headers = raw_data[0]
        self.data = raw_data[1:]

    def load_data(self, filename):
        with open(filename) as open_file:
            csv_reader = csv.reader(open_file)
            return list(csv_reader)

    def find_mean(self, list_of_values):
        return mean


iris = Iris("iris.csv")

print(iris.headers)
print(iris.data)

iris.find_mean()
