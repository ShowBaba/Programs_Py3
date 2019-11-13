import csv

score_list = []
grade_list = []

with open('result_data.csv', 'r') as opened_file:
    data_list = list(csv.reader(opened_file))
    # print(data_list)
    individual_data = data_list[1:-1]  # individual_data variable stores
    # the data list except the header and the last element list which is the unit list
    print(individual_data)


for item in individual_data:
    individual_data_strip =  item[2:]
    print(individual_data_strip)


