# Write a function that will read in the iris dataset
# Write a function that will return the mean for each 'column'
# Write a function that will write the means to a new csv file

import csv


def read_iris(csvfile):
    try:
        with open("iris.csv", "r") as opened_file:
            csvreader = csv.reader(opened_file)
            headers = next(csvreader)
            print(headers)
            for row in csvreader:
                print(row)

    except FileNotFoundError:
        print("Error: File not found!")
        raise


my_read_iris = read_iris("iris.csv")


def column_mean(csvfile, reader):
    with open("iris.csv", "r") as opened_file:
        csv_reader = list(csv.reader(opened_file))

        csv_reader = csv_reader[1:]
        column_means = []
        for i in range(0, 4):
            sum = 0
            for row in csv_reader:
                print(i, row)
                sum += float(row[i])
            mean = sum / (len(list(csv_reader)))
            column_means.append(mean)
        return column_means


print(column_mean("iris.csv", my_read_iris))

iris_means = column_mean("iris.csv", read_iris("iris.csv"))
iris_means_headers = f"[sepal_length, {iris_means[0]}], [sepal_width, {iris_means[1]}],[petal_length, {iris_means[3]}]," \
                     f"[petal_width, {iris_means[4]}] "


def write_iris_mean():
    with open("iris_means.csv", "w") as csvfile:
        csvfile.write(iris_means_headers)

