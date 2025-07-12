# Prompt the user for monthly income
income = float(input("Enter your monthly income: "))

# Prompt the user for monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
Monthly_savings = income - expenses

# Calculate projected savings after one year with 5% interest
projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly savings are ${Monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
