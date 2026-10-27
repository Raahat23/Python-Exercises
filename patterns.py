# printing out patterns using a for loop

# number of rows the pattern should have
rows = int(input("Enter the number of rows for pattern: "))

# symbol used to draw pattern
pattern_symbol = input("Select the pattern symbol you want(*, +, $, @): ")

# implementing a for loop to draw out the patterns
for i in range(1, rows + 1):
    for j in range(i):
        print(pattern_symbol, end=" ")
    print()