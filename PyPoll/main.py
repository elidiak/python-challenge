#To start off, we need to import several files. Especially Math
#import math
import os
import csv

#We need to initialize each variable to hold the results expected in the final output
'''Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''

total_votes = 0
candidate0_name = "Charles Casper Stockham"
candidate0_percent = 0.0
candidate0_votes = 0
candidate1_name = "Diana DeGette"
candidate1_percent = 0.0
candidate1_votes = 0
candidate2_name = "Raymon Anthony Doane"
candidate2_percent = 0.0
candidate2_votes = 0
winner_name = ""
csvpath = os.path.join(os.getcwd(),'Resources','election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    ''' Core for each loop needs to count the vote for each candidate, and add to the total vote tally and per candidate tally
    '''
    for row in csvreader:
        if row[2] == candidate0_name:
            total_votes += 1
            candidate0_votes += 1
        elif row[2] == candidate1_name:
            total_votes += 1
            candidate1_votes += 1
        else:
            total_votes += 1
            candidate2_votes += 1
            
'''Determine vote percentages'''
if total_votes != 0:
    candidate0_percent = 100 * (candidate0_votes / total_votes)
    candidate1_percent = 100 * (candidate1_votes / total_votes)
    candidate2_percent = 100 * (candidate2_votes / total_votes)
else:
    print("Total Votes is 0")

'''Determine the winner'''
if candidate0_votes > candidate1_votes and candidate0_votes > candidate2_votes :
    winner_name = candidate0_name
elif candidate1_votes > candidate0_votes and candidate1_votes > candidate2_votes :
    winner_name = candidate1_name
else:
    winner_name = candidate2_name

'''We need to print the results to the terminal'''
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"{candidate0_name}: {candidate0_percent}% ({candidate0_votes})")
print(f"{candidate1_name}: {candidate1_percent}% ({candidate1_votes})")
print(f"{candidate2_name}: {candidate2_percent}% ({candidate2_votes})")
print("----------------------------")
print(f"Winner: {winner_name}")
print("----------------------------")

'''We need to print the results to a text file'''
output_path = os.path.join(os.getcwd(), 'Analysis', "election_results.txt")

with open(output_path, 'w') as file:
    #copy of block above to the file
    file.write("Election Results")
    file.write("----------------------------")
    file.write(f"Total Votes: {total_votes}")
    file.write("----------------------------")
    file.write(f"{candidate0_name}: {candidate0_percent}% ({candidate0_votes})")
    file.write(f"{candidate1_name}: {candidate1_percent}% ({candidate1_votes})")
    file.write(f"{candidate2_name}: {candidate2_percent}% ({candidate2_votes})")
    file.write("----------------------------")
    file.write(f"Winner: {winner_name}")
    file.write("----------------------------")