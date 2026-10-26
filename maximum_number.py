# find the maximum and minimum number amongst a list of numbers

numbers = [2, 4, 6, 8, 7 , 5, 9, 10, 15, 1, 0, 3, 11]

largest_number = numbers[0]
smallest_number = numbers[0]

# finding the largest or maximum number
for i in numbers:
    if i > largest_number:
        largest_number = i
print(f"The largest number in the list is: {largest_number}")


#finding the smallest or minimum number
for i in numbers:
    if i < smallest_number:
        smallest_number = i
print(f"The smallest number in the list is: {smallest_number}")
    
