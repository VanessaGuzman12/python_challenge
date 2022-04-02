import os
import csv
#path2= os.path.join('Resources','budget_data.csv')
path2="C:/Users/vanem/Homeworks/HomeworkPython/python_challenge/PyPoll/Resources/election_data.csv"

#def load_file (filepath):
with open (path2,'r') as data:
    csvreader = csv.reader(data, delimiter=',')
    header = next(csvreader)
    #print(f"Header: {header}")
        #return data.read()

    records= []
    for row in csvreader:
        records.append(row)

num_votes=len(records)
print("Total Votes: ", num_votes)

candidates=[]
for i in range(0,num_votes):
    if records[i][2] in candidates:
        candidates==candidates
    else:
        candidates.append(records[i][2])
print (candidates)

votes_candidate= []
for i in range(len(candidates)):
     votes_candidate.append(0)

for i in range(num_votes):
    for j in range(len(candidates)):
        if records[i][2]== candidates[j]:
            votes_candidate[j]+=1

print (votes_candidate)





