from audioop import avg
import os
import csv
#path2= os.path.join('Resources','budget_data.csv')
path2="C:/Users/vanem/Homeworks/HomeworkPython/python_challenge/PyBank/Resources/budget_data.csv"

#def load_file (filepath):
with open (path2,'r') as data:
    csvreader = csv.reader(data, delimiter=',')
    header = next(csvreader)
    print(f"Header: {header}")
        #return data.read()
    
    records= []
    for row in csvreader:
        records.append(row)

num_months=len(records)
print("Total Months: ", num_months)

total_amount= 0
for i in range(0, num_months):
    total_amount+=int(records[i][1])
print ("Total: ", total_amount)

avg_list= []
for i in range(0,num_months-1):
    change= int(records[i+1][1])-int(records[i][1])
    avg_list.append(change)

avg_change=sum(avg_list)/len(avg_list)
print("Average Change: ", avg_change)

date_increase= records[0][0]
greatest_increase= int(records[0][1])
for i in range(0,num_months):
    if greatest_increase < int(records[i][1]):
        greatest_increase= int(records[i][1])
        date_increase= records[i][0]
print("Greatest Increase in Profits: ",date_increase, greatest_increase)

date_decrease= records[0][0]
greatest_decrease= int(records[0][1])
for i in range(0,num_months):
    if greatest_decrease > int(records[i][1]):
        greatest_decrease= int(records[i][1])
        date_decrease= records[i][0]
print("Greatest Decrease in Profits: ",date_decrease, greatest_decrease)

    
    
    
    
    
    #number_months= int (bank_record)
    #average= int(bank_record)
    #greatest_increase =int (bank_record)
    #greatest_decrease=int (bank_record)








    

#load_file(path2)


