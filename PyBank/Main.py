import os
import csv

# create file path 
file = os.path.join('Data', 'Budget_Data' + '.csv')

#empty lists for revenues and months 
revenue = []
months = []


#read and parse csv file
with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader, None)

    for row in csv_reader:
        months.append(row[0])
        revenue.append(int(row[1]))

#The total number of months included in the dataset
total_months = len(months)

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = revenue[0]

#The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = revenue[0]

#The total net amount of "Profit/Losses" over the entire period
total_revenue = 0

#loop through revenue and compare number to find greatest increase and decrease
#+add each revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        greatest_inc_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        greatest_dec_month = months[r]
    total_revenue += revenue[r]

#The average change in "Profit/Losses" between months over the entire period
average_change = round(total_revenue/total_months, 2)

#set path for output file
output_file = os.path.join('Output','pybank_output' + '.txt')

# open output file in write mode and print the summary
with open(output_file, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + greatest_inc_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + greatest_dec_month + ' ($' + str(greatest_decrease) + ')')

#open output file in read mode and print to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
