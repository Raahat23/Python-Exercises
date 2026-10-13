# Calculate a person's age from their birth year

# Ask user for their birth year
birth_year = int(input("In which year were you born? "))

# Ask user for the current year
present_year = int(input("Which year is it presently? "))

age = present_year - birth_year

print(f"Your age is: {age}")