# The data need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. THe winner of the election based on popular vote.

# Import the datetime class from the datetime module
#import datetime as dt
# Use now() attribute on the datetime class to get the present time
#now = dt.datetime.now()
# Print the present time
#print("The time right now is ", now)

# Add our dependencies
import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save a file to a path.
file_to_save = os.path.join('Analysis','election_analysis.txt')

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the csv file.
    #for row in file_reader:
    #    print(row)

# Using the with statement, open the file as a text file.
#with open(file_to_save,'w') as txt_file:

    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
