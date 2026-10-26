# Multiplication Table

# Ask user to input the number they would like to generate the table for
number = int(input("Enter a number (interger): "))

for i in range(1, 13):
    print(f"{number} * {i} = {number * i}")