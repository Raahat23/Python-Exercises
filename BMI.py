# A program to calculate the body mass index (BMI) of a person

# Ask user for their weight in Kg
weight = float(input("Enter your weight in kg: "))

# Ask user for their height in meters
height = float(input("Enter your height in meters: "))

BMI_meters = round(((weight)/(height*height)), 2)

print(f"Your Body Mass Index is: {BMI_meters}")