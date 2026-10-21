# Personal Expense Calculator:
# defining varialbles

# Ask user for their monthly income
income = float(input("What is your monthly income? "))

# amount spend on rent for the month
rent = float(input("How much did you soend n rent? "))

# amount spent on food for the month
food = float(input("How much was spent on food? "))

# amount spent on transport for the month
transport = float(input("How much did you spend on transportation? "))

# amount spent on utilities for the 
utilities = float(input("Enter the amount spent on utilities: "))

# amount spent on entertainment for the month
entertainment = float(input("Amount Spent on entertainment: "))

# amount spent on shopping for the month
shopping = float(input("How much was spent on personal items: "))

# Calculate total expenses
total_expenses = rent + food + transport + utilities + entertainment + shopping

# calculate the remaining income after expenses
remaining_income = income - total_expenses

# savings
savings = remaining_income

# savings percentage
savings_percentage = (savings / income) * 100

# display output
print(f"Total Expenses: {total_expenses}")
print(f"Remaining Income: {remaining_income}")
print(f"Savings: {savings}")
print(f"Percentage of income dedicated to savings: {savings_percentage}%")