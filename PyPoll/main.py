# Python code to help a small, rural town modernize its vote counting process
import os
import csv

# The file path to election_data.csv (composed of three columns: Voter ID, County, and Candidate)
datapath = os.path.join("Resources", "election_data.csv")

# Analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who recieved votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

total = 0
candidates = []
votes = []
percentage = []
winner = 0
samecandidate = False

# Read in the CSV module
with open(datapath) as data:
    datareader = csv.reader(data, delimiter=",")
    dataheader = next(datareader)

    # Read each row of data after the header
    for row in datareader:
        #Increase the total number of votes by 1
        total = total + 1

        # Compare list of candidates and add to list if new
        for candidate in candidates:
            if candidate == row[2]:
                # Increase number of votes for that candidate
                votes[candidates.index(candidate)] = votes[candidates.index(candidate)] + 1
                # Set samecandidate = True so we do not create a new candidate
                samecandidate = True
        if samecandidate == False:
            candidates.append(row[2])
            votes.append(1)
        else:
            samecandidate = False

# Calculate the percentage of votes each candidate won
for vote in votes:
    percentage.append((vote / total)*100)

    # Calculate the winner of the election based on popular vote
    if vote > votes[winner]:
        winner = votes.index(vote)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {round(percentage[candidates.index(candidate)], 3)}% ({votes[candidates.index(candidate)]})")
print("-------------------------")
print(f"Winner: {candidates[winner]}")
print("-------------------------")

# Export a text file with the results
# Set the export file path
exportpath = os.path.join("analysis", "output.txt")
# Open the output file and write the same results that were printed to the terminal
with open(exportpath, "w", newline="") as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total}\n")
    output.write("-------------------------\n")
    for candidate in candidates:
        output.write(f"{candidate}: {round(percentage[candidates.index(candidate)], 3)}% ({votes[candidates.index(candidate)]})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {candidates[winner]}\n")
    output.write("-------------------------\n")
    output.close()
