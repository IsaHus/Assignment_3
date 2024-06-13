import os
import csv
current_directory = os.getcwd()

filename = os.path.join("budget_data.csv")

print(filename)

month_count = 0
net_total = 0
changes_in_profit_losses = []
previous_profit_loss = None 

with open(filename,'r') as file:
  csv_reader = csv.reader(file, delimiter=',')

  next(csv_reader)
 
  for row in csv_reader:
  
    month_count += 1
    profit_losses= int(row[1])
    net_total += profit_losses

    if previous_profit_loss is not None:
      change = profit_losses - previous_profit_loss
      changes_in_profit_losses.append(change)
    
    previous_profit_loss = profit_losses
  
total_months = month_count 
average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)  
greatest_increase = max(changes_in_profit_losses) 
greatest_decrease = min(changes_in_profit_losses) 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")  
print(f"Greatest Increase in Profits: {month_count-changes_in_profit_losses.index(greatest_increase)} ({greatest_increase})") 
print(f"Greatest Decrease in Profits: {month_count-changes_in_profit_losses.index(greatest_decrease)} ({greatest_decrease})") 
