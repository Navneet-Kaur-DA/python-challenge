import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    
    net_total=0
    profit_loss=[]
    changes=[]
    revenue_total=0
    month=[]
    change_month=[]
    greatest_increase=0
    greatest_decrease=0
    greatest_increase_month=0
    greatest_decrease_month=0

    # Loop through the data
    for row in csvreader:
        net_total=net_total+int(row[1]) #calculate total value
        profit_loss.append(int(row[1])) #saving second column to perform various calculations
        month.append(row[0]) #saving first column to calculate total months

    
    #loop to go through profit_loss cloumn to calculate the difference 
    for i in range(1,len(profit_loss)): 
        changes.append(profit_loss[i]-profit_loss[i-1])
        change_month.append(month[i])
        

    #using max and min function to calculate maximun and minimum values of difference array(changes)
    greatest_increase=max(changes)
    greatest_decrease=min(changes)

    #loop to find the dates of max and min value
    for i in range(1,len(changes)):
        if(changes[i]==greatest_increase):
            greatest_increase_month=change_month[i]
        if(changes[i]==greatest_decrease):
            greatest_decrease_month=change_month[i]
    
    #calculating the average
    revenue_total=round(sum(changes)/len(changes),2)


    #printing the final results to the terminal
    print("Financial Analysis\n")
    print("---------------------------\n")
    print(f"Total Months: {len(month)}")
    print(f"Total :${net_total}")   
    print(f"Average Change:${revenue_total}")     
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")  
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")  

    #openning txt file in write mode and writing all the results to the txt file
    file=open("analysis/Final_report.txt","w")
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(" Total Months :" +str( len(month)) +"\n")
    file.write(" Total :$"+str( net_total) +"\n")
    file.write(" Average Change :$"+str( revenue_total) +"\n")
    file.write(" Greatest Increase in Profits:" +str(greatest_increase_month)+" ("+str(greatest_increase) +")\n")
    file.write(" Greatest Decrease in Profits :" +str(greatest_decrease_month)+" ("+str(greatest_decrease) +")\n")
    