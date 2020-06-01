# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# importing csv module 
import os
import csv 


# Path to file  
filename = os.path.join('election_data.csv')

# txt file name
textfile = "election_data.txt"

# Read in the CSV file
with open(filename) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
#Define Values to Variables, per LA Session and Documentation Referral
    total_votes = []
    voter_id = []
    candidates = []
    vote_percent = []
    khan = []
    correy = []
    li = []
    otooley = []     
     
    for row in csvreader:
        voter_id.append(int(row[0])
        #candidates.append(row[2])
    
    total_votes = (len(voter_id))
    print(total_votes)
#
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley) 
        print(khan_votes)
        print(correy_votes)
        print(li_votes)
        print(otooley_votes)
         
        
        
 #Identify and Group Candidates to Count Vote for Each - Utilize index per LA Session and add to vote count 
    #if candidate in candidate_id:
        #candidate_list = candidate_id.index(candidate)
        #andidate_votes[candidate_list] = candidate_votes[candidate_list] + 1
    #else:
        #candidate_id.append(candidate)
        #candidate_votes.append(1)
#Calculate Percentage      
        #for i in range(len(candidate_list)):
         #vote_percent = candidate_votes[i] / total_votes
         #vote_percent.append(pct)
     #Votes by Person      
            
            
            
        
        
    
        
    