import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_vote=0
    candidates=[]
    candidate_votes=[]
    candidate_name=[]
    per=[]
    max_votes=0


    #loop to go through all the values to count total votes and saving Candidate names in array
    for row in csvreader:
        total_vote=total_vote+1
        candidates.append(row[2])


    #loop to add candidate names to the array    
    for name in candidates:
        if not name in candidate_name: #if name is already in the array , dont add the name to array. add only if name is not there already
            candidate_name.append(name)

    #loop through candidate_name array to count all the votes to each candidate and calculate percantage    
    for j in range(0,len(candidate_name)):
        name=candidate_name[j]
        candidate_votes.append(candidates.count(name))
        vper=(candidate_votes[j]/total_vote)*100
        per.append(vper)


    #printing resuts on terminial        
    print("Election Results\n")
    print("-----------------------------\n")
    print("Total Votes "+str(total_vote))  
    print("-----------------------------\n")


    for i in range(0,len(candidate_name)):
        print(str(candidate_name[i])+":  "+str(round((per[i]),3))+"%  ("+str(candidate_votes[i])+")")
       
       
    print("-----------------------------\n")
    max_votes=(max(candidate_votes))

    #for loop to find the name of the candidate who got maximum votes
    for j in range(0,len(candidate_name)):
        if(candidate_votes[j]==max_votes):
            print("Winner :"+str(candidate_name[j]))

    print("-----------------------------\n")       

    #opening txt file in write mode and writing all the results in txt file
    file=open("analysis/Election_results.txt","w") 
    file.write("Election Results\n")
    file.write("---------------------------\n")
    for i in range(0,len(candidate_name)):
        file.write(str(candidate_name[i])+":  "+str(round((per[i]),3))+"%  ("+str(candidate_votes[i])+")\n")
    file.write("---------------------------\n")
    for j in range(0,len(candidate_name)):
        if(candidate_votes[j]==max_votes):
            file.write("Winner :"+str(candidate_name[j])+"\n")

    file.write("-----------------------------\n")       



    