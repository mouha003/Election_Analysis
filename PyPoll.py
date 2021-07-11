#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

#Import the datetime calss from the datetime module

import datetime as dt
# Use the now() attribute on the datetime calss to get the present time.

now = dt.datetime.now()

# Print the present time.
print("The time right now is ", now)

import csv
import os
dir(csv)

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file.
# with open(file_to_load) as election_data:
#     print(election_data)


# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file 
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     header = next(file_reader)
     print(header)
     for row in file_reader:
         print(row)
         break



