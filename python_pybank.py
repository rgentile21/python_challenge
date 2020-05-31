# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:45:04 2020

@author: Gentile
"""
# importing csv module 
import os
import csv 

# csv file name 
filename = "budget_data.csv"

# txt file name
textfile = "budget_data.txt"

# Read in the CSV file
with open(filename) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
#Define Values to Variables, per LA Session and Documentation Referral
    monthyr = []
    revenue = []
    rev_change = []
    month_change = []

#Months Count
    for row in csvreader:
        monthyr.append(row[0])
        revenue.append(row[1])
   #print(len(monthyr))
    
#Utilized Map() function per LA Documentaton referral
#Sum Total Value of Profit/Loss    
#for row in csvreader(not needed moved to above section)
    revtotal_abs = map(int,revenue)
    total_revenue = (sum(revtotal_abs))
   #print(total_revenue)
    
#Average Change
    p = 0
    for p in range(len(revenue) - 1):
        profit_loss = int(revenue[p+1]) - int(revenue[p])
        rev_change.append(profit_loss)
        Total = sum(rev_change)
        month_change = Total / len(rev_change)
       #print(month_change)
        #If print() is used shows all values of the column
        
#Greatest Increase in Profits: Month/Yr with Dollar Amount in ()
#Utilized index() function per LA Session and Documentation Referral
        increase_profit = max(rev_change)
        print(increase_profit)
        x = rev_change.index(increase_profit)
        increase_month = monthyr[x+1]
        
#Greatest Decrease in Profits 
        decrease_profit = min(rev_change)
        print(decrease_profit)
        y = rev_change.index(decrease_profit)
        decrease_month = monthyr[y+1]
        
#Print Financial Information (Syntax from Wrestler Example)
        print(f'Financial Analysis'+'\n')
        print(f'--------------------------'+'\n')
        print("Total Months: " + str(len(monthyr)))
        print("Total: $"+ str(total_revenue))
        print("Average Change: $"+ str(month_change))
        print(f"Greatest Increase in Profits: {increase_month} (${increase_profit})")
        print(f"Greatest Decrease in Profits: {decrease_month} (${decrease_profit})")
    
    
    
text_file=open(textfile,"w")
# Output to text file
text_file.write('budget_data.txt') 
text_file.write("Financial Analysis'+'\n")
text_file.write("--------------------------'+'\n")
text_file.write("Total Months: " + str(len(monthyr)) + "\n")
text_file.write("Total: $"+ str(total_revenue) + "\n")
text_file.write("Average Change: $"+ str(month_change) + "\n")
text_file.write("Greatest Increase in Profits: + str(increase_month) ($(increase_profit)" + "\n")
text_file.write("Greatest Decrease in Profits: + str(decrease_month) ($(decrease_profit)" + "\n")
text_file.close()
    
   #print(output)    
        
#Export text file
#with open(textfile,"w") as txt_file:
   #txt_file.write(output)
        
        
   
        
                   
        

