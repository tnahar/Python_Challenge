import csv
import os

path = ("/Users/Taslemun/Python/Case Assignment /Resources/budget_data.csv")
output = ("/Users/Taslemun/Python/Case Assignment /output.txt")
budget_csv = os.path.join(path)

total_months = 0
prev_rev = 0 
monthchange = []
revchange = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0



with open(budget_csv) as rev_data:
    reader = csv.DictReader(rev_data)
  
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row["Profit/Losses"])
              
       
        revchangesto = int(row["Profit/Losses"]) - prev_rev
        prev_rev = int(row["Profit/Losses"])
        revchange = revchange + [revchangesto]
        monthchange = monthchange + [row["Date"]]
        
if (revchangesto > greatest_increase [1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revchangesto


avgrev = sum(revchange) / len(revchange)

outputinfo = (
    f"\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Rev: ${revchange}\n"
    f"Average Change: ${avgrev}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits {greatest_decrease[0]} (${greatest_decrease[1]})\n" 
    )

print(outputinfo) 
    with open(output, "w") as txt_file:
        txt.file.write(output)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    