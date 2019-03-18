import os
import csv

bankCSV = os.path.join("..", "Resources", "budget_data.csv")

months = 0
total = 0
change = 0
changeList = []
maxChange = 0
minChange = 0
averageChange = 0

with open(bankCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        months = months + 1
        total = total + row[1]
        changeList.append(row[1] - change)
        change = row[1]

maxChange = max(changeList)
minChange = min(changeList)
averageChange = sum(changeList) / len(changeList)

f = open("bankSummary.txt", "w+")
f.write("Financial Analysis")
f.write("------------------------------")
f.write("Total Months: " + months)
f.write("Total: " + total)
f.write("Average Change: " + averageChange)
f.write("Greatest Increase in Profits: " + maxChange)
f.write("Greatest Decrease in Profits: " + maxChange)
f.close()
