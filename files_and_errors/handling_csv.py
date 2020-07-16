# csv = comma separated values

import csv
scores = []
with open("some_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
#     headers = list(map(str.lstrip, next(csvreader)))
#     # next moves us one along in an iterable - gets rid of header
#     # map lets us strip white space from each item in list
#     for row in csvreader:
#         scores.append(int(row[-1]))
#
# print(headers)
# print(scores)
    print(list(csvreader))  # prints each line as a list, in another list

data_to_write = [["David", 5], ["Paula", 6], ["Nish", 7]]

with open("new_data.csv", "w") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_to_write)
