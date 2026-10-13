# Calculate the compund Interest
# CI: Compund Interest
# P: Initial Principal Amount (Starting balance)
# r: Annual Interest Rate written as a decimal (divide the percentage by 100)
# n: The number of times the interest compunds per year
# t: The total time the money is invested or borrowed, measured in years

# Ask user for principal amount
P = float(input("What's the principal: "))

# Ask user for interest rate in perecentage
r = int(input("What's the interest rate: "))

# Ask user for number of times the interest compounds per year (eg., 1 for yearly, 12 for monthly)
n = int(input("Number of times the interest compounds per year (eg., 1 for yearly, 12 for monthly); "))

# Ask user for the total time the money is invested or borrowed, measured in years.
t = int(input("The total time the money is invested or borrowed, measured in years: "))

# converting the rate into a decimal
r = r / 100

# Multiplying the compunding frquency by time
nt = n * t

CI = round((P * (1 + (r / n)) ** nt), 2)

print(f"The compound interest is: ${CI}")