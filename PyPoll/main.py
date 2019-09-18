import os
import csv



#open file
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

f=open('PyPollResults.txt', 'w')

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    Candidates = {}
    TotalVotes = 0
    MostVotes = 0
    PctofVotes = 0
    Winner = ""
    OutputTxt = ""

    for row in csvreader:
                     
        #Count votes cast
        candidate = row[2]
        TotalVotes += 1
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1

 
    #print to terminal and write to file
    OutputTxt = f"""\n Election Results \r
    ------------------------------\r
    Total Votes: {TotalVotes}\r
    ------------------------------\r"""


    print(OutputTxt)
    f.write(OutputTxt)

    #total votes by candidate
    for candidate in Candidates:
        Candidates[candidate] 

        #Percent of votes for each candidate
        PctofVotes = (Candidates[candidate])/(TotalVotes) * 100
        
        print(f"{candidate}: {int(PctofVotes)}% ({Candidates[candidate] })")
        f.write(f"""{candidate}: {int(PctofVotes)}% ({Candidates[candidate]})\r""" )

        #determine winning candidate
        if Candidates[candidate] > MostVotes:
            Winner = candidate
            MostVotes = Candidates[candidate]

            

#print to terminal and write to file
OutputTxt = f"""------------------------------ \r
Winner:  {Winner} \r
------------------------------"""


print(OutputTxt)
f.write(OutputTxt)
f.close