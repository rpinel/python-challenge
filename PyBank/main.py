# Modules
import os
import csv


#Declare Variables
total_months = 0
total        = 0
v_max        = 0
v_min        = 0
total_revenue_change = 0

#csvpath = os.path.join("..", "Resources", "budget_data.csv")

print('\n Financial Analysis\n' + '-' *30)

with open("budget_data.csv") as f:
    reader = csv.reader(f)
    next(reader)
    revenue_data = []
    date_data    = []
    for row in reader:
        
        date_data.append(row[0])
        revenue_data.append(row[1])
        total+=int(row[1])
   #Total Months     
    total_months = len(revenue_data) 
    print(f'Total Months: {total_months}')
    #Total Revenue
    print(f'Total: ${format(total,",.2f")}')

   #Average change Revenue
revenue = 0
for x in range(len(revenue_data)):
    total_revenue_change+=int(revenue_data[x]) - revenue
    revenue = int(revenue_data[x])
   
total_avg_change = (total_revenue_change - int(revenue_data[0])) / ( total_months -1 )
print(f'Average Change: ${format(total_avg_change,",.2f")}')
   
  # greatest increase in revenue
high_revenue = 0
for x in range(len(revenue_data)):
    if int(revenue_data[x]) - int(revenue_data[x - 1]) > high_revenue:
        high_revenue = int(revenue_data[x]) - int(revenue_data[x - 1])
        high_month = date_data[x]

print(f'Greatest Increase in Revenue:, {high_month}, (${format(high_revenue,",.2f")})')

 # greatest decrease in revenue
low_revenue = 0
for x in range(len(revenue_data)):
    if int(revenue_data[x]) - int(revenue_data[x - 1]) < low_revenue:
        low_revenue = int(revenue_data[x]) - int(revenue_data[x - 1])
        low_month = date_data[x]

print(f'Greatest Increase in Revenue:, {low_month}, (${format(low_revenue,",.2f")})')

with open('budget.txt',"w") as txt_file:
    txt_file.write(f'\n Financial Analysis\n' + '-' *30)
    txt_file.write(f'\nTotal Months: {total_months}')
    txt_file.write(f'\nTotal: ${format(total,",.2f")}')
    txt_file.write(f'\nAverage Change: ${format(total_avg_change,",.2f")}')
    txt_file.write(f'\nGreatest Increase in Revenue:, {high_month}, (${format(high_revenue,",.2f")})')
    txt_file.write(f'\nGreatest Increase in Revenue:, {low_month}, (${format(low_revenue,",.2f")})')
