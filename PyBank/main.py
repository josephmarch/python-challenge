# A Python script for analyzing the financial records of your company
import os
import csv

# The file path to budget_data.csv (which is composed of two columns: Date and Profit/Losses)
datapath = os.path.join("Resources", "budget_data.csv")

# Analyze the records to calculate each of the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period (calculated), then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period

months = 0
total = 0
changes = []
dates = []
lastmonth = 0
increase = 0
increasedate = ""
decrease = 0
decreasedate = ""
firstrow = True

# Read in the CSV module
with open(datapath) as budget:
    budgetreader = csv.reader(budget, delimiter=',')
    budgetheader = next(budgetreader)

    # Read each row of data after the header
    for row in budgetreader:
        # Increase number of months by one
        months = months + 1
        # Increase total to eventually sum all profit/losses
        total = total + int(row[1])
        # For the first row we need to set the lastmonth value before going forward, but only for the first row,
        # this will make it so our later code for calculating the changes list shows correct values in changes[0]
        if firstrow == True:
            lastmonth = int(row[1])
            firstrow = False
        else:
            # Add changes in profit/losses to the changes list to later be averaged
            changes.append(int(int(row[1]) - lastmonth))
            # Set lastmonth to this month's value to be used next loop
            lastmonth = int(row[1])
        # Collect the dates in a list
        dates.append(row[0])

# Calculate the average
ave = sum(changes) / len(changes)

# Find the greatest increase and greatest decrease (date and amount)
for i in range(len(changes)):
    if int(changes[i]) > int(increase):
        increase = int(changes[i])
        increasedate = dates[i+1]
    if int(changes[i]) < int(decrease):
        decrease = int(changes[i])
        decreasedate = dates[i+1]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${round(total,2)}")
print(f"Average Change: ${round(ave,2)}")
print(f"Greatest Increase in Profits: {increasedate} (${increase})")
print(f"Greatest Decrease in Profits: {decreasedate} (${decrease})")

# Export a text file with the results
# Set the export file path
exportpath = os.path.join("analysis", "output.txt")
# Open the output file and write the same results that were printed to the terminal
with open(exportpath, "w", newline="") as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {months}\n")
    output.write(f"Total: ${round(total,2)}\n")
    output.write(f"Average Change: ${round(ave,2)}\n")
    output.write(f"Greatest Increase in Profits: {increasedate} (${increase})\n")
    output.write(f"Greatest Decrease in Profits: {decreasedate} (${decrease})\n")
    output.close()
