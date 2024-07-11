#To start off, we need to import several files. Especially Math
#import math
import os
import csv

#We need to initialize each variable to hold the results expected in the final output
'''Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

total_months = 0
total_difference = 0
months = []
profit = []
average_change = 0
greatest_increase_date = ""
greatest_increse_profit = 0
greatest_decrease_date = ""
greatest_decrease_profit = 0

'''Read in the csv file that we need to analyze. There's two columns
Month and profit or loss'''

csvpath = os.path.join(os.getcwd(), 'Resources', "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    cvsreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(cvsreader)

    ''' We need to read in each value from the csv file. Once that is loaded, we can do work on it
    '''
    for row in cvsreader:
        months.append(row[0])
        profit.append(row(1))

'''Core logic loop to start calcualating the values. We start at months and profit 1, the second row in the csv'''
i = 1

for i in len(months):
    
    #add 1 to total months
    total_months += 1
    #calculate the difference for each month from month -1
    total_difference = total_difference + profit(i)-profit(i-1)
    #If difference is greater than greatest increase, change the variables
    if greatest_increase_profit < profit(i) - profit (i-1):
        greatest_increase_profit = profit(i) - profit(i-1)
        greatest_increase_date = months(i)
        #If difference is greater than greatest increase, change the variables
    if greatest_decrease_profit > profit(i) - profit (i-1):
        greatest_decrease_profit = profit(i) - profit(i-1)
        greatest_decrease_date = months(i)
    
#calculate average change
average_change = total_difference / total_months

'''We need to print the results to the terminal'''
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_difference}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increse_profit})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease_profit})")

'''We need to print the results to a text file'''
output_path = os.path.join(os.getcwd(), 'Analysis', "financial_analysis.txt")

with open(output_path, 'w') as file:
    #copy of block above to the file
    file.print("Financial Analysis")
    file.print("----------------------------")
    file.print(f"Total Months: {total_months}")
    file.print(f"Total: {total_difference}")
    file.print(f"Average Change: {average_change}")
    file.print(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increse_profit})")
    file.print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease_profit})")

