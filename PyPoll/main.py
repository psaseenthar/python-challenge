import os
import csv

voteCSV = os.path.join("..", "Resources", "election_data.csv")

count = 0
countKhan = 0
countCorrey = 0
countLi = 0
countOtooley = 0
winner = ""

with open(voteCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        count = count + 1
        if row[2] == "Khan":
            countKhan = countKhan + 1
        elif row[2] == "Correy":
            countCorrey = countCorrey + 1
        elif row[2] == "Li":
            countLi = countLi + 1
        elif row[2] == "O'Tooley":
            countOtooley = countOtooley + 1

if countKhan > countCorrey and countKhan > countLi and countKhan > countOtooley:
    winner = "Khan"
elif countCorrey > countKhan and countCorrey > countLi and countCorrey > countOtooley:
    winner = "Correy"
elif countLi > countKhan and countLi > countCorrey and countLi > countOtooley:
    winner = "Li"
elif countOtooley > countKhan and countOtooley > countCorrey and countOtooley > countLi:
    winner = "O'Tooley"

f = open("voteSummary.txt", "w+")
f.write("Election Results")
f.write("------------------------------")
f.write("Total Votes: " + count)
f.write("------------------------------")
f.write("Khan: " + round(countKhan) + "(" + countKhan + ")")
f.write("Correy: " + round(countCorrey) + "(" + countCorrey + ")")
f.write("Li " + round(countLi) + "(" + countLi + ")")
f.write("O'Tooley: " + round(countOtooley) + "(" + countOtooley + ")")
f.write("------------------------------")
f.write("Winner: " + winner)
f.write("------------------------------")
f.close()

