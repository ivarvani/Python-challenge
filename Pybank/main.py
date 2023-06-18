"""
csv module
"""
#imported csv and os modules
import os

import csv

budget_data_path = os.path.join("Resources","budget_data.csv")
with open(budget_data_path, encoding="UTF-8") as csv_file:
    input_data = csv.reader(csv_file, delimiter=",")
    headers = next(input_data) # this is our columns headers row
    line_count = 0  # number of rows in our data whuch eqauls to the months
    total = 0  # the net earned
    difference = 0
    difference_list = [] # list  to get the changes across the entire period
    for row in input_data:
        if line_count == 0:
            line_count += 1
            total = int(row[1])
            row_value_before = int(row[1])
            highest_change = 0
            lowest_change = 0
            difference = 0
            count_of_difference = 0
        else:
            # print(f'{" , ".join(row)}')
            line_count += 1
            total += int(row[1])
            difference = int(row[1]) - (row_value_before)
            difference_list.append(difference)
            count_of_difference += 1
            #print(f'{",".join(row)}   {difference}')
            row_value_before = int(row[1])
            if difference > highest_change:
                highest_change = difference
                month = row[0]
            if difference < lowest_change:
                lowest_change = difference
                new_month = row[0]

    #printing the results on the terminal
    months = f"Number of Months = {line_count }"
    print (months)
    net = f"Net total = {total}"
    print(net)
    positive_change = f"Greatest positive change :{month}  {highest_change}"
    print(positive_change)
    negative_change =f"Greatest negative change :{new_month}  {lowest_change}"
    print(negative_change)
    average = (sum(difference_list)/len(difference_list))
    print(f'the average change : {average :.2f}')
    #writing the results to analysis
    text_file_path ="Analysis/Analysis.txt"
    with open(text_file_path,'w',encoding='UTF-8') as text_file:
        text_file.write("Financial Analysis")
        text_file.write("\n----------------------------------------")
        text_file.write("\n" + months)
        text_file.write("\n"+ net)
        text_file.write("\n" + positive_change)
        text_file.write("\n" + negative_change)
        text_file.write("\n" f'The average change : {average :.2f}')
