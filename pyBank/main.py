import os
import csv
        

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

with open(csvpath, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader)


        Months = 0
        Total_Rev_Change = 0
        Previous_Revenue = 0
        Present_Revenue = 0
        Revenue_Change = 0
        Max_Revenue_Change = 0
        Min_Revenue_Change = 0
        Total_Revenue = 0

        for row in csvreader:
            
            
            Months = Months + 1
            Total_Revenue = float(Total_Revenue) + float(row[1])
            Present_Revenue = row[1]
            Revenue_Change = float(Present_Revenue) - float(Previous_Revenue)
            Total_Rev_Change = Total_Rev_Change + Revenue_Change
            Previous_Revenue = row[1]

            if Revenue_Change > Max_Revenue_Change:
                Max_Revenue_Change = Revenue_Change
                MaxRevMonth = row[0]
            if Revenue_Change < Min_Revenue_Change:
                Min_Revenue_Change = Revenue_Change
                MinRevMonth = row[0]

        AvgRevChange = Total_Rev_Change/Months

        #Output to terminal
        print()
        print()
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {Months}")
        print(f"Total Revenue: ${round(Total_Revenue,2)}")
        print(f"Average Revenue Change: ${round(AvgRevChange,2)}")
        print(f"Greatest Increase in Profits: {MaxRevMonth} (${round(Max_Revenue_Change,2)})")
        print(f"Greatest Decrease in Profits: {MinRevMonth} (${round(Min_Revenue_Change,2)})")
        print()

        #Output to file
        f=open("PyBankOutput.txt", 'w')
        f.write("Financial Analysis\r")
        f.write("----------------------------\r")
        f.write(f"Total Months: {Months}\r")
        f.write(f"Total Revenue: ${round(Total_Revenue,2)}\r")
        f.write(f"Average Revenue Change: ${round(AvgRevChange,2)}\r")
        f.write(f"Greatest Increase in Profits: {MaxRevMonth} (${round(Max_Revenue_Change,2)})\r")
        f.write(f"Greatest Decrease in Profits: {MinRevMonth} (${round(Min_Revenue_Change,2)})\r")
        f.close

