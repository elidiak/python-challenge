#To start off, we need to import several files. Especially Math
import math
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
total_profit = 0
average_profit = 0
greatest_increase_date = 0
greatest_increse_profit = 0
greatest_decrease_date = 0
greatest_decrease_profit = 0

'''Read in the csv file that we need to analyze. There's two columns
Month and profit or loss'''
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    ''' Core for each loop needs to interate over the entire loaded file. We need a sum of all profits, a look behind to check for greatest profit increase and decrease
    and to calculate the average profit
    '''
    for row in csvreader:
        print(row)

