import os
import csv
#path= os.path.join('Resources','budget_data.csv')
path2="C:/Users/vanem/Homeworks/HomeworkPython/python_challenge/PyBank/Resources/budget_data.csv"
path_output="C:/Users/vanem/Homeworks/HomeworkPython/python_challenge/PyBank/Analysis/budget.txt"

with open (path2,'r') as data:
    csvreader = csv.reader(data, delimiter=',')
    header = next(csvreader)
    print(f"Header: {header}")
        
    
    records= []
    for row in csvreader:
        records.append(row)

num_months=len(records)
#print("Total Months: ", num_months)

total_amount= 0
for i in range(0, num_months):
    total_amount+=int(records[i][1])
#print ("Total: ", total_amount)

avg_list= []
for i in range(0,num_months-1):
    change= int(records[i+1][1])-int(records[i][1])
    avg_list.append(change)

avg_change=sum(avg_list)/len(avg_list)
#print("Average Change: ", avg_change)

date_increase= records[0][0]
greatest_increase= int(records[0][1])
for i in range(0,num_months):
    if greatest_increase < int(records[i][1]):
        greatest_increase= int(records[i][1])
        date_increase= records[i][0]
#print("Greatest Increase in Profits: ",date_increase, greatest_increase)

date_decrease= records[0][0]
greatest_decrease= int(records[0][1])
for i in range(0,num_months):
    if greatest_decrease > int(records[i][1]):
        greatest_decrease= int(records[i][1])
        date_decrease= records[i][0]
#print("Greatest Decrease in Profits: ",date_decrease, greatest_decrease)

print ("Financial Analysis")
print("_______________________")
print("Total Months: ", num_months)
print ("Total: ", total_amount)
print("Average Change: ", avg_change)
print(f"Greatest Increase in Profits: {date_increase} ${greatest_increase:,.2f}")
print(f"Greatest Decrease in Profits: {date_decrease} ${greatest_decrease:,.2f}")
  
file=open(path_output,'w')
file.write(f"Financial Analysis\n____________________\nTotal Months:  {num_months}\nTotal:  ${total_amount:,.2f}\nAverage Change:  ${avg_change:,.2f}\nGreatest Increase in Profits: {date_increase} (${greatest_increase:,.2f})\nGreatest Decrease in Profits: {date_decrease} (${greatest_decrease:,.2f})")
file.close()
    
    
    
  








    




