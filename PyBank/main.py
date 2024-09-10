import csv
import os

# Path to the file
file_to_load = os.path.join(r"PyBank/Resources/budget_data.csv")

# Set initial variables
total_months = 0
total_profit_loss = 0
previous_month_profit_loss = None
monthly_changes = []
greatest_increase = {"month": "", "amount": float('-inf')}
greatest_decrease = {"month": "", "amount": float('inf')}

# Open and read the CSV file
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    
    for row in reader:
        total_months += 1
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss
        
        # Calculate the monthly change
        if previous_month_profit_loss is not None:
            change = current_month_profit_loss - previous_month_profit_loss
            monthly_changes.append(change)
            
            # Update greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["month"] = row[0]
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["month"] = row[0]
                greatest_decrease["amount"] = change
        
        previous_month_profit_loss = current_month_profit_loss

# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Print output statement
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})\n"
)
print(output)